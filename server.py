import socket
import select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 10500


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]
clients = {}

def recv_exact(sock, n):
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

def receive_message(client_socket):
    try:
        message_header = recv_exact(client_socket, HEADER_LENGTH)
        if not message_header:
            return False
        message_length = int(message_header.decode("utf-8").strip())
        message_data = recv_exact(client_socket, message_length)
        if not message_data:
            return False
        return {"header": message_header, "data": message_data}
    except:
        return False

while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            user = receive_message(client_socket)
            if user is False:
                continue
            sockets_list.append(client_socket)
            clients[client_socket] = user
            print(f"{client_address[0]}:{client_address[1]} username: {user['data'].decode('utf-8')}")
        else:
            message = receive_message(notified_socket)
            if message is False:
                print(f"Disconnected: {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            user = clients[notified_socket]
            for client_socket in clients.copy():
                if client_socket != notified_socket:
                    try:
                        client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
                    except:
                        client_socket.close()
                        sockets_list.remove(client_socket)
                        del clients[client_socket]

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
