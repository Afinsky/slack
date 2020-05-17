!#/bin/bash


aws lambda update-function-code --function-name $LAMBDA_FUNCTION_NAME --zip-file fileb://function.zip
