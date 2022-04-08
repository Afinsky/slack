import json
import boto3
import os
import urllib3
import logging
import configparser

SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']
SLACK_CHANNEL = os.environ['SLACK_CHANNEL']
SLACK_USER = os.environ['SLACK_USER']

http = urllib3.PoolManager()
logger = logging.getLogger()
config = configparser.ConfigParser()
config.read("config.ini")

def getBranchInfo(pipeline):
    client = boto3.client('codepipeline')
    execution = client.get_pipeline(
        name=pipeline
    )
    message = json.dumps(execution['pipeline']['stages'][0]['actions'][0]['configuration']['BranchName'], indent=4, sort_keys=True, default=str, separators=(',', ': '))
    return json.loads(message)

def getApplicationDestinationURL(config, configName, pipelineName):
    try:
        return config[configName][pipelineName]
    except KeyError:
        return "Not exist"

def getCommitInfo(pipeline, executionId, infoType):
    client = boto3.client('codepipeline')
    execution = client.get_pipeline_execution(
        pipelineName=pipeline,
        pipelineExecutionId=executionId
    )
    message = json.dumps(execution['pipelineExecution']['artifactRevisions'][0][infoType], indent=4, sort_keys=True, default=str, separators=(',', ': '))
    if infoType == 'revisionSummary':
        message = json.loads(message) #Remove special/escape characters
        message = json.loads(message) #Convert string to dictionary
        message = message['CommitMessage']
    else:
        message = json.loads(message)
    return message

def codepipelineHandler(event):
    subject = "AWS CodePipeline Notification"
    fields = []
    color = "warning"
    changeType = ""
    #snsSubject = event['Records'][0]['Sns']['Subject']

    message = event['Records'][0]['Sns']['Message']
    message = json.loads(message)
    detailType = message['detail-type']

    if detailType == "CodePipeline Pipeline Execution State Change":
        changeType = ""
    elif detailType == "CodePipeline Stage Execution State Change":
        changeType = "STAGE " + message['detail']['stage']
    elif detailType == "CodePipeline Action Execution State Change":
        changeType = "ACTION"

    if message['detail']['state'] == "SUCCEEDED":
        color = "good"
    elif message['detail']['state'] == "FAILED":
        color = "danger"

    header = message['detail']['state'] + ": CodePipeline " + changeType

    fields.append({"title": "Message",
                   "value": header,
                   "short": False})
    fields.append({"title": "Pipeline",
                   "value": message['detail']['pipeline'],
                   "short": True})
    fields.append({"title": "Region",
                   "value": message['region'],
                   "short": True})
    fields.append({"title": "Status Link",
                   "value": "https://console.aws.amazon.com/codepipeline/home?region=" + message['region'] + "#/view/" +
                            message['detail']['pipeline'],
                   "short": False})
    #pipeline=message['detail']['pipeline']
    fields.append(
        {
            "title": "Branch",
            "value": getBranchInfo(
                        pipeline=message['detail']['pipeline']
                    ),
            "short": False
        }
    )
    fields.append(
        {
            "title": "Commit message",
            "value": getCommitInfo(
                        pipeline=message['detail']['pipeline'],
                        executionId=message['detail']['execution-id'],
                        infoType='revisionSummary'
                   ),
            "short": False
         }
    )
    fields.append(
        {
            "title": "Commit hash",
            "value": getCommitInfo(
                        pipeline=message['detail']['pipeline'],
                        executionId=message['detail']['execution-id'],
                        infoType='revisionId'
                    ),
            "short": False
        }
    )
    fields.append(
        {
            "title": "Commit URL",
            "value": getCommitInfo(
                        pipeline=message['detail']['pipeline'],
                        executionId=message['detail']['execution-id'],
                        infoType='revisionUrl'
                    ),
            "short": False
        }
    )
    fields.append(
        {
            "title": "Destination link",
            "value": getApplicationDestinationURL(
                config=config,
                configName="Applications",
                pipelineName=message['detail']['pipeline']
            ),
            "short": False
        }
    )

    message = event['Records'][0]['Sns']['Message']
    message = json.loads(message)
    header = message['detail']['state'] + ": CodePipeline " + message['detail']['pipeline']

    fields.append({"title": "Message",
                   "value": header,
                   "short": False})
    #fields.append({"title": "Detail",
    #               "value": message,
    #               "short": False})

    slackMessage = {
        'channel': SLACK_CHANNEL,
        'username': SLACK_USER,
        "text": "*" + subject + "*",
        "attachments": [
            {
                "color": color,
                "fields": fields
            }
        ]
    }
    return slackMessage


def codebuildHandler(event):

    message = json.dumps(event['Records'][0]['Sns']['Message'])

    return message


def lambda_handler(event, context):
    logger.info("Event: " + str(event))

    json_data = json.loads(event['Records'][0]['Sns']['Message'])
    eventSource = json_data['source']

    if "codepipeline" in eventSource:
        slack_message = codepipelineHandler(event)

    if "codebuild" in eventSource:
        slack_message = codebuildHandler(event)

    http.request('POST', SLACK_WEBHOOK_URL, body=json.dumps(slack_message),
                 headers={'Content-Type': 'application/json'})
    return