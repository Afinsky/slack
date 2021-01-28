FROM node:13.12.0-alpine3.10

#RUN apk add --update
RUN npm install -g serverless@2.17.0
COPY package.json ./
RUN npm install
RUN apk add --no-cache \
        python3 \
        py3-pip \
    && pip3 install --upgrade pip \
    && pip3 install \
        awscli \
    && rm -rf /var/cache/apk/*
#WORKDIR /app
ENTRYPOINT ["serverless"]
#COPY ./src ./
CMD ["--version"]