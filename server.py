const express = require('express');
const http = require('http');
const WebSocket = require('ws');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

wss.on('connection', (ws) => {
    console.log('Client connected');

    ws.on('message', (message) => {
        console.log('Received from Unity:', message);
    });

    // Example: Send a command to Unity to call a function with parameters
    setTimeout(() => {
        ws.send(JSON.stringify({ functionName: "MovePlayer", parameters: { x: 5, y: 10 } }));
    }, 5000); // Send a command 5 seconds after connection
});

server.listen(3000, () => {
    console.log('Server running on port 3000');
});
