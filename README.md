### Environment variables:

`SLACK_CHANNEL` <br>
`SLACK_USER` <br>
`SLACK_WEBHOOK_URL` <br>

## Schema
![](https://github.com/Afinsky/slack/blob/master/schema.png?raw=true)


## CloudWatch event pattern rule

```
{
  "source": [
    "aws.codepipeline"
  ],
  "detail-type": [
    "CodePipeline Pipeline Execution State Change"
  ],
  "detail": {
    "state": [
      "FAILED",
      "SUCCEEDED"
    ]
  }
}
```
