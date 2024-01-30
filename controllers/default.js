// Import the 'node-pty' module for creating pseudo-terminals
const Pty = require('node-pty');

// Exported function for installing routes
exports.install = function () {
    // Define a route for the root path '/'

    ROUTE('/');
    
    ROUTE('GET /tests', function(){
        this.json({
            message : "This is a test route"
        })
    });

    // Define a WebSocket route for handling communication over a WebSocket connection 
    ROUTE('SOCKET /', WebSocketHandler, ['raw']);

};

// WebSocket handler function
function WebSocketHandler() {

    var self = this;
    
    // Disable encoding and decoding for raw WebSocket communication
    self.encodedecode = false;

    // Automatically destroy the WebSocket connection when it is closed
    self.autodestroy();

    // Event handler for when a Websocket connection is opened
    self.on('open', function(client) {
        // Create a new pseudo-terminal for each client
        client.tty = Pty.spawn('pyton3', ['main.py'], {
            name: 'xterm-color',
            cols: 120,
            rows: 30,
            cwd: process.env.PWD,
            env: process.env
        });

        // Event handler for when the pseudo-terminal exits
        client.tty.on('exit', function(code, signal) {
            // clean up resources when the terminal exits
            client.tty = null;
            client.close();
        });

        // Event handler for when data is received fron the pseudo-terminal
        client.tty.on('data', function(data) {
            // Send the received data to the WebSocket client
            client.send(data);
        });
    });

    // Event handler for when a WebSocket connection is closed
    self.on('close', function(client) {
        // Kill the pseudo-terminal if it exists
    }) 
