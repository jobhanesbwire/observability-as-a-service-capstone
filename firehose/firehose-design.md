# Kinesis Data Firehose Design

Flow: CloudWatch Logs → Subscription Filter → Kinesis Data Firehose → S3

Benefits:
- Centralization: collect logs from EC2, ECS, RDS into a single archival store.
- Long-term retention: S3 lifecycle policies for cost-effective storage.
- Auditability: immutable log archives for post-incident analysis.
- Analytics: use Athena/Glue to query archived logs.

Notes:
- Use placeholders for bucket names (e.g., `REPLACE_LOG_ARCHIVE_BUCKET`).
- Ensure Firehose has permission to write to the S3 bucket and to decrypt with KMS if used.
