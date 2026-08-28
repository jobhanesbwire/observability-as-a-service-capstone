# Failure Testing

Safe, controlled tests to validate observability and automation.

## Simulated 500 errors
- Call `/simulate-error` on the ECS app. Expect HTTP 500 responses, ErrorCount increase, and logs showing structured ERROR.

## Latency tests
- Call `/simulate-latency?delay=7000` to generate a 7s response. Expect latency metrics and traces in X-Ray.

## ECS CPU load
- Run a controlled CPU worker inside a task (e.g., stress-ng) in a test environment and monitor CPUUtilization alarm.

## ErrorCount generation
- Emit structured error logs from the application to verify metric filter and alarm behavior.

For each test, capture screenshots of CloudWatch metrics, Logs Insights queries, and alarm state changes to include in the final report.
