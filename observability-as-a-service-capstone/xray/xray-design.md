# AWS X-Ray Design

Trace flow:
- Client → ALB → ECS application → RDS

What X-Ray helps with:
- Latency analysis and distribution across services
- Identifying failed requests and error hotspots
- Visualizing service dependencies and bottlenecks
- Correlating traces with logs for root-cause analysis

Note: Instrumentation is required in the application (X-Ray SDK) and the ALB/ECS integration. Trace data screenshots and traces will be added after deployment.
