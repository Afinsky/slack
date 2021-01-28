import json
import requests

def hello(event, context):
    r = requests.get("http://ip-api.com/json/")

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        #"input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "content": r.text
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
