!#/bin/bash


pip3 install --target ./package requests

cd package/

zip -r9 ${OLDPWD}/function.zip .

cd $OLDPWD

zip -g function.zip lambda_function.py

aws lambda update-function-code --function-name slack --zip-file fileb://function.zip
