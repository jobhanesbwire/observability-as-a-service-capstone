# EventBridge Rules

Example EventBridge rule patterns and purposes.

1) CloudWatch Alarm -> Lambda/SNS

Example pattern (match alarm state change to ALARM):

```
{
  "source": ["aws.cloudwatch"],
  "detail-type": ["CloudWatch Alarm State Change"],
  "detail": {
    "state": { "value": ["ALARM"] }
  }
}
```

2) ECS Task Failure

Pattern for ECS task state change events that indicate failures.

```
{
  "source": ["aws.ecs"],
  "detail-type": ["ECS Task State Change"],
  "detail": { "lastStatus": ["STOPPED"] }
}
```

Use targets to invoke remediation Lambdas or SNS topics. Replace account-specific values and ARNs when deploying.
