# Architecture Overview

```mermaid
graph LR
  Internet --> ALB["Application Load Balancer"]
  ALB --> EC2["EC2 Web Tier"]
  ALB --> ECS["ECS Fargate App Tier"]
  ECS --> RDS["RDS MySQL"]

  subgraph Observability
    EC2 --> CW["CloudWatch"]
    ALB --> CW
    ECS --> CW
    RDS --> CW
    CW --> Insights["Logs Insights / Dashboards"]
    CW --> XRay["X-Ray"]
    CW --> Firehose["Kinesis Data Firehose -> S3"]
    CW --> Alarms["Alarms -> EventBridge -> Lambda/SNS"]
  end

  Firehose --> S3["S3 Archive"]
  Alarms --> EventBridge --> Lambda
  EventBridge --> SNS["SNS -> On-call"]
```

Flows:
- Ingress: Internet → ALB → EC2/ECS
- Observability: Metrics & Logs from EC2/ALB/ECS/RDS flow into CloudWatch. Logs can be exported via Firehose to S3 for archival and analytics.
- Tracing: X-Ray captures distributed traces from ALB → ECS → RDS.
- Automation: CloudWatch alarms emit events to EventBridge which routes to Lambda remediation functions or SNS for notifications.
