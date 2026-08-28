# CloudWatch Alarms

This document describes recommended alarms and their purpose.

1) ECS CPU Utilization High
- Metric: `AWS/ECS -> CPUUtilization` (per service or cluster)
- Threshold: `> 80%`
- Evaluation: 2 datapoints within 5 minutes
- Purpose: Detect sustained CPU pressure on Fargate tasks.
- Expected action: Create EventBridge event on ALARM -> trigger Lambda remediation and notify via SNS.

2) ALB HTTP 5xx Rate
- Metric: `AWS/ApplicationELB -> HTTPCode_Target_5XX_Count` (aggregate)
- Threshold: `> 5` errors per minute (adjust to environment)
- Evaluation: 2 datapoints within 5 minutes
- Purpose: Detect backend/server errors observed by ALB.
- Expected action: EventBridge -> SNS for on-call; optionally trigger automated investigation Lambda.

3) Application ErrorCount
- Metric: Namespace `ObservabilityCapstone`, Metric `ErrorCount`
- Threshold: `> 10` within 5 minutes
- Evaluation: 1 datapoint of 5 minutes
- Purpose: Detect spikes in application-level errors from log metric filters.
- Expected action: EventBridge -> Lambda remediation and SNS notification.

EventBridge integration:
- Configure rules that match CloudWatch Alarm state changes ("ALARM") and forward to targets (Lambda, SNS).

SNS / Lambda response:
- Use SNS for human on-call paging.
- Use Lambda for automated remediation actions (e.g., restart unhealthy ECS tasks, tag EC2 instance for investigation).

Placeholders:
- Replace topic ARNs, Lambda ARNs, and role ARNs in configuration when deploying.
