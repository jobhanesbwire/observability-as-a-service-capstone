const express = require('express');

const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.json({
    application: 'observability-ecs-app',
    message: 'The ECS application is running',
    status: 'healthy'
  });
});

app.get('/health', (req, res) => {
  res.status(200).json({
    status: 'healthy'
  });
});

app.get('/simulate-error', (req, res) => {
  const errorLog = {
    level: 'ERROR',
    message: 'Simulated application failure',
    timestamp: new Date().toISOString(),
    route: '/simulate-error'
  };

  console.log(JSON.stringify(errorLog));

  res.status(500).json({
    error: 'This is a simulated failure for the observability capstone.'
  });
});

app.get('/simulate-latency', async (req, res) => {
  const delayMs = 5000;

  await new Promise((resolve) => setTimeout(resolve, delayMs));

  const latencyLog = {
    level: 'INFO',
    message: 'Simulated latency',
    latency_ms: delayMs,
    timestamp: new Date().toISOString(),
    route: '/simulate-latency'
  };

  console.log(JSON.stringify(latencyLog));

  res.status(200).json({
    status: 'healthy',
    message: 'Simulated latency completed successfully',
    latency_ms: delayMs
  });
});

app.listen(port, () => {
  const startupLog = {
    level: 'INFO',
    message: 'ECS application started',
    port,
    timestamp: new Date().toISOString()
  };

  console.log(JSON.stringify(startupLog));
});

module.exports = app;
