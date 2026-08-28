# Implementation Guide (Concise Checklist)

Sections below provide short actionable steps for each major area.

## Networking
- Prepare VPC, public/private subnets, and NAT as required.

## EC2 / ALB
- Launch EC2 instances for web tier and install CloudWatch Agent.
- Create ALB and target group pointing to EC2 and ECS targets.

## ECS
- Build and push Docker image from `app/ecs-app/`.
- Create ECS cluster and Fargate service behind ALB.

## RDS
- Launch private RDS MySQL instance.

## CloudWatch
- Create log groups and install the CloudWatch agent (see `cloudwatch/cloudwatch-agent-config.json`).
- Add metric filters and dashboards.

## X-Ray
- Instrument application and enable X-Ray tracing for ECS tasks.

## Firehose
- Create Firehose delivery stream to S3 and subscribe CloudWatch Logs.

## Alarms
- Create alarms documented in `cloudwatch/alarms.md` and connect to EventBridge/SNS.

## EventBridge / Lambda
- Deploy Lambda functions and roles; create EventBridge rules to trigger remediation.

## Dashboard
- Import `dashboards/observability-dashboard.json` and replace placeholders.
