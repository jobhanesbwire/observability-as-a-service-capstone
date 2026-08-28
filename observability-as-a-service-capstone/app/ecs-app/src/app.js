const express = require('express');
const morgan = require('morgan');

const app = express();
const port = process.env.PORT || 3000;

// Structured logging middleware
app.use(morgan('combined'));

app.get('/', (req, res) => {
  res.json({
    application: 'observability-ecs-app',
    environment: process.env.NODE_ENV || 'development',
    message: 'Welcome to the ECS application sample'
  });
});

app.get('/health', (req, res) => {
  res.json({ status: 'healthy' });
});

app.get('/simulate-error', (req, res) => {
  const errLog = {
    level: 'ERROR',
    message: 'Simulated application failure',
    timestamp: new Date().toISOString()
  };
  // Emit structured error to logs
  console.error(JSON.stringify(errLog));
  res.status(500).json({ error: 'Simulated failure' });
});

app.get('/simulate-latency', async (req, res) => {
  const delayMs = parseInt(req.query.delay) || 7000; // default 7s
  await new Promise(r => setTimeout(r, delayMs));
  console.log(JSON.stringify({ level: 'INFO', message: 'Simulated latency', latency_ms: delayMs, timestamp: new Date().toISOString() }));
  res.json({ status: 'delayed', latency_ms: delayMs });
});

app.listen(port, () => {
  console.log(JSON.stringify({ level: 'INFO', message: 'Server started', port, timestamp: new Date().toISOString() }));
});
