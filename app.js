// PROTOTYPE PACKET LISTENER

const express = require('express'),
      dgram = require('dgram'),
      app = express(),
      socket = dgram.createSocket('udp4')

socket.on('listening', () =>{
    let addr = socket.address();
    console.log(`Listening for UDP packets at ${addr.address}:${addr.port}`);
});

socket.on('error', (err) => {
    console.error(`UDR error: ${err.stack}`);
});

socket.on('message', (msg) => {
    parsedMsg = JSON.parse(msg.toString());
    console.log(parsedMsg);
    console.log('Received UDP Message');
});

app.set('port', 3000);
socket.bind(5005)