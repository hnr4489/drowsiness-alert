const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

let alertLogs = [];

app.post('/log', (req, res) => {
    const newAlert = { status: req.body.status, timestamp: new Date().toLocaleTimeString() };
    alertLogs.unshift(newAlert);
    console.log("🚨 ALERT RECEIVED:", newAlert); // THIS MUST APPEAR IN TERMINAL 1
    res.status(200).send("OK");
});

app.get('/logs', (req, res) => {
    res.json(alertLogs);
});

app.listen(5000, "0.0.0.0", () => console.log("✅ Server alive on Port 5000"));
module.exports = app;
