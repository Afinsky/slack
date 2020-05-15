from lambda_function import lambda_handler

event = {
    "Records": [
        {
            "EventVersion": "1.0",
            "EventSubscriptionArn": "arn:aws:sns:us-east-1:868292153463:dev-roofle-slack:d5c5982f-eb85-4da3-b63e-fd2a0972c357",
            "EventSource": "aws:sns",
            "Sns": {
                "SignatureVersion": "1",
                "Timestamp": "2020-05-12T14:35:08.182Z",
                "Signature": "S7tCB8iuCp0gNAGiclGtin+42K3NKdAKboToVm0lMaCuLx2hm+bJlRH9uyxM5zz5l2mtGsVNfi3HaWYkVNQClCY5GDXsavAUu8sSVbIUYQsVoUP5VzePnUOUDqWahSYhw1N3LmKL+txhoEYGGj0I9Nev2IZw273noGvChC4WjNvpe1O7+S5aE2zfnK1nZPBB/wORPWeqTxYxvzU2jjnWOIY1lw/pIlyqUyXlxOPSCsWLVwdF8bA+3ItJ05UXmsF81AXHlvWYgF2+z0bxzL440vhdAp0PJr9835hOT9E0nDYTfmGE3/xwZ3jDLI4GqLkO7QWJF8V3GHT+jep+K7Pj2Q==",
                "SigningCertUrl": "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-a86cb10b4e1f29c941702d737128f7b6.pem', u'MessageId': u'cdf7e008-dd13-566c-82be-b73c6b4fffcf",
                "Message": {
                    "version": "0",
                    "id": "CWE-event-id",
                    "detail-type": "CodePipeline Pipeline Execution State Change",
                    "source": "aws.codepipeline",
                    "account": "123456789012",
                    "time": "2017-04-22T03:31:47Z",
                    "region": "us-east-1",
                    "resources": [
                        "arn:aws:codepipeline:us-east-1:123456789012:pipeline:myPipeline"
                    ],
                    "detail": {
                        "pipeline": "myPipeline",
                        "version": "1",
                        "state": "STARTED",
                        "execution-id": "01234567-0123-0123-0123-012345678901"
                    }
                },
                "MessageAttributes": {},
                "Type": "Notification",
                "UnsubscribeUrl": "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:868292153463:dev-roofle-slack:d5c5982f-eb85-4da3-b63e-fd2a0972c357",
                "TopicArn": "arn:aws:sns:us-east-1:868292153463:dev-roofle-slack",
                "Subject": "null"
            }
        }
    ]
}

context = None

lambda_handler(event, context)
