const Pty = require('node-pty');

exports.install = function() {

    // Route to views/index
    ROUTE('/');
    // WebSocket route
    ROUTE('SOCKET /', webSocketHandler, ['raw']);

};

function webSocketHandler() {

    var self = this;

    self.encodedecode = false;
    self.autodestroy();

    self.on('open', function(client) {

        // Each client will have own terminal
        client.tty = Pty.spawn('python3', ['run.py'], { 
            name: 'xterm-color', 
            cols: 120, 
            rows: 30, 
            cwd: process.env.PWD, 
            env: process.env 
        });

        client.tty.on('exit', function(code, signal) {
            // What now?
            client.tty = null;
            client.close();
        });

        client.tty.on('data', function(data) {
            client.send(data);
        });

    });

    self.on('close', function(client) {
        if (client.tty) {
            client.tty.kill(9);
            client.tty = null;
        }
    });

    self.on('message', function(client, msg) {
        client.tty && client.tty.write(msg);
    });
}
