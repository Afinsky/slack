### Environment variables:

`SLACK_CHANNEL` <br>
`SLACK_USER` <br>
`SLACK_WEBHOOK_URL` <br>


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
