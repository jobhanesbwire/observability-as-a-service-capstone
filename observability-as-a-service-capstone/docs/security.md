# Security Considerations

- Follow least-privilege for IAM roles and policies.
- Do not hardcode credentials in code or Dockerfiles; use IAM roles and Secrets Manager.
- Keep RDS in private subnets and restrict access via security groups.
- Encrypt logs at rest (CloudWatch) and objects in S3 with KMS as required.
- Protect S3 log buckets with MFA delete/versioning and appropriate lifecycle policies.
- Ensure Lambda functions have minimal permissions and log all actions for auditability.
