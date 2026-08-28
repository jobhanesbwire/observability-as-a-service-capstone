# CloudWatch Metric Filters

Example metric filter for application ERROR logs.

- Log Group: `/observability/ecs/application`
- Filter pattern: `ERROR` (or JSON pattern matching `$.level = "ERROR"`)

Example CloudWatch metric created from the filter:

- Namespace: `ObservabilityCapstone`
- Metric Name: `ErrorCount`
- Metric Value: `1` for each matched log event

Suggested Alarm: trigger when `ErrorCount > 10` within a 5 minute period.

Notes: Use JSON-based filter when logs are structured (recommended). This enables reliable counting of application errors.
