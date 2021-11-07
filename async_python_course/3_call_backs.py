import selectors
import socket

selector = selectors.DefaultSelector()  # works in the same way as function select()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5001))
    server_socket.listen()

    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)
    # if you want to pass function as object, do not use parentheses: foo(data=accept_connection)


def accept_connection(server_socket):
    client_socket, addr, = server_socket.accept()
    print(f'Connected successfully with {addr}')
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)


def send_message(client_socket):

    request = client_socket.recv(4096)

    if request:
        response = 'Hello from server socket\n'.encode()
        client_socket.send(response)
    else:
        client_socket.unregister()
        client_socket.close()


def event_loop():
    while True:

        events = selector.select()  # select() return a tuple like (key, events) for each registered obj
        # where key - is object of SelectorKey(namedtuple)
        # SelectorKey is used to connect within socket an event and to it related data. It has following fields:
        # fileobj
        # events
        # data
        for key, _ in events:
            call_back = key.data
            call_back(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()
