# socketProgramming

# Socket Programming Chat Application

This project implements a basic multi-client chat application using Python sockets and the `select` module. It consists of a server and client that can communicate over a network.

## Features

- Real-time text-based messaging
- Supports multiple clients using non-blocking sockets
- Handles client disconnections gracefully
- Uses message headers for clean message parsing

## Files

- `server.py` – The server program that handles incoming client connections and message broadcasting.
- `client.py` – The client program that connects to the server and enables users to send/receive messages.

## Requirements

- Python 3.x

## How to Run

1. **Start the Server**

   Open a terminal and run:


2. **Start the Client(s)**

Open another terminal and run:


Enter a username when prompted and start chatting.

3. **Multiple Clients**

You can open multiple terminals and run `client.py` to simulate multiple users.

## Notes

- The server must be running before starting any clients.
- IP and Port should match between server and client (`127.0.0.1` and `10500` by default).
- This is a console-based app meant for learning socket programming concepts.

## Author

Chamal Promoddya
