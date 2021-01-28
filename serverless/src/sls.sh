#!/usr/bin/env bash

docker build -t serverless \
      -f ./../docker/build/main/Dockerfile ./ > /dev/null
docker run -it --rm \
      -w /app \
      -v $PWD:/app \
      -v $HOME/.aws/:/home/node/.aws/ \
      -u $(id -u ${USER}):$(id -g ${USER}) \
      serverless $@
      #--entrypoint sh \
      #-e AWS_CONFIG_FILE=/tmp/.aws/config \
      #-e AWS_SHARED_CREDENTIALS_FILE=/tmp/.aws/credentials \


