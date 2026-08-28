# Cleanup Order

A safe cleanup order to avoid orphaned resources and unexpected charges:

1. Stop and remove ECS services and tasks
2. Delete ALB and target groups
3. Delete RDS instances (snapshot if needed)
4. Delete Firehose delivery streams
5. Empty and delete S3 log archive buckets
6. Remove Lambda functions
7. Remove EventBridge rules
8. Remove SNS topics and subscriptions
9. Delete CloudWatch alarms, dashboards, and log groups
10. Terminate EC2 instances
11. Remove security groups
12. Delete VPC (last)

Check Billing / Cost Explorer after cleanup.
