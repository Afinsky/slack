import json
import os
import urllib3
import logging

SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']
SLACK_CHANNEL = os.environ['SLACK_CHANNEL']
SLACK_USER = os.environ['SLACK_USER']

http = urllib3.PoolManager()
logger = logging.getLogger()


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