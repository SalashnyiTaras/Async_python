"""
assync code - runs within one process within one thread
useful for I/O problems - reading writing to dbs, files, working with internets

буфер отправки (clients' method .send() ) - сохраняет в себя сообщения от клиента. После получения сообщения,
с него нужно считать сообщения, чтобы получить следующие сообщения

blocking functions - block execution of a program until they are completed, until they return.
When blocking function is finished - it returns also контроль выполнения программы
"""

import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5001))
server_socket.listen()

while True:
    client_socket, addr, = server_socket.accept()  # accept - is blocking function
    print(f'Connected successfully with {addr}')

    while True:
        request = client_socket.recv(4096)  # recv - is also blocking function

        if not request:
            break
        else:
            response = 'Hello from server socket\n'.encode()
            client_socket.send(response)  # recv - is also blocking function
