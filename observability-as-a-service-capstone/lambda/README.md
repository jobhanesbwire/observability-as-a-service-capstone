This folder contains example Lambda functions used for automated remediation and investigation workflows.

Workflows:
- CloudWatch Alarm → EventBridge rule → Lambda (remediation)
- CloudWatch Alarm → SNS → on-call

Files:
- `ecs-remediation/lambda_function.py` — stops an unhealthy ECS task to force replacement.
- `ec2-tag-remediation/lambda_function.py` — tags EC2 instances for investigation.

Ensure appropriate IAM roles and least-privilege policies are attached when deploying these functions.
