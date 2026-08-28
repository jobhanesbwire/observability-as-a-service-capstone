# CloudWatch Logs Insights - Useful Queries

## Error spike detection
Query: Find and count ERROR level messages over time.

```
fields @timestamp, @message
| filter @message like /ERROR|Error|Error:/
| stats count() by bin(5m)
| sort @timestamp desc
```
Helps detect spikes of error volume across services.

## HTTP 5xx analysis
Query: Extract status codes from access logs and aggregate 5xx.

```
fields @timestamp, @message
| parse @message /(?<status>\d{3})/ 
| filter status >= 500 and status < 600
| stats count() by status, bin(5m)
```
Helps identify when the ALB or application returns server errors.

## Top application errors
Query: Group by error message to find most frequent failures.

```
fields @timestamp, @message
| filter @message like /ERROR|Error/
| parse @message "*\"message\": \"*\"" as err
| stats count() as occurrences by err
| sort occurrences desc
| limit 20
```

## Latency analysis
Query: Find slow requests and their distribution.

```
fields @timestamp, @message
| parse @message /latency_ms\":\s*(?<latency>\d+)/
| filter latency is not null
| stats pct(95, latency) as p95, avg(latency) as avgLatency by bin(5m)
```
This helps detect latency regressions and when to investigate traces in X-Ray.
