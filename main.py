from lambda_function import lambda_handler
import json

# Opening JSON file
f = open('event.json')

# Returns JSON object as a dictionary
event = json.load(f)

# Closing file
f.close()

context = None
lambda_handler(event, context)
