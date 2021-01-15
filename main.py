from lambda_function import lambda_handler


event= {
  "Records": [
    {
      "EventSource": "aws:sns",
      "EventVersion": "1.0",
      "EventSubscriptionArn": "arn:aws:sns:us-east-1:123456789123:CodePipelineNotifications:00000000-0000-0000-0000-000000000000",
      "Sns": {
        "Type": "Notification",
        "MessageId": "00000000-0000-0000-0000-000000000000",
        "TopicArn": "arn:aws:sns:us-east-1:123456789:codepipeline-alerts",
        "Subject": "None",
        "Message": "{\"version\":\"0\",\"id\":\"00000000-0000-0000-0000-000000000000\",\"detail-type\":\"CodePipeline Pipeline Execution State Change\",\"source\":\"aws.codepipeline\",\"account\":\"123456789123\",\"time\":\"2018-02-14T07:14:14Z\",\"region\":\"us-east-1\",\"resources\":[\"arn:aws:codepipeline:us-east-1:123456789123:a-pipeline-project\"],\"detail\":{\"pipeline\":\"dev-roofle-api\",\"execution-id\":\"34b1920a-0ac7-424d-8cf1-36f5711707a3\",\"state\":\"STARTED\",\"version\":1.0}}",
        "Timestamp": "2018-02-14T07:14:27.208Z",
        "MessageAttributes": {}
      }
    }
  ]
}









context = None

lambda_handler(event, context)
