# Incident Response

Guidance for common incidents and automated responses.

## Application 5xx spike
- Detect via ALB 5xx metric and ErrorCount.
- EventBridge triggers SNS for on-call and Lambda for automated investigation (collect logs, tag instances).

## High ECS CPU
- Alarm triggers EventBridge → Lambda to scale or replace tasks (or notify on-call).

## Repeated application errors
- Metric filter increments ErrorCount; when threshold exceeded, invoke remediation and create an incident ticket.

## ECS task failure
- EventBridge listens for ECS task STOPPED events and can trigger automated recovery or notify operators.

## Database performance degradation
- Monitor RDS CPU, latency, connections. Notify DBAs and escalate via SNS.
