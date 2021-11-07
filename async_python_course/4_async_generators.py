""" Sponsored by David Beazley in 2015 at PyCon - 'Concurrency from the Ground up Live' """
from select import select
import socket

tasks = []  # list of generators

# we get from them generators using select() and add them to tasks queue.
# they will contain a pair socket: generator

to_read = {}
to_write = {}


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5001))
    server_socket.listen()

    while True:

        yield ('read', server_socket)
        client_socket, addr, = server_socket.accept()
        print(f'Connected successfully with {addr}')

        tasks.append(client(client_socket))


def client(client_socket):
    while True:

        yield ('read', client_socket)
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'Hello from server socket\n'.encode()

            yield ('write', client_socket)
            client_socket.send(response)

    client_socket.close()


def event_loop():

    while any([tasks, to_read, to_write]):

        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])
            # select works in a way that every iterable object passed in function being iterated over and
            # if smh appears in iterable object, its key being taken and unpacked forming variable

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)

            reason, sock = next(task)  # ('read'/'write', server_socket) my comment

            if reason == 'read':
                to_read[sock] = task
            if reason == 'write':
                to_write[sock] = task
        except StopIteration:
            print("Done")


tasks.append(server())
event_loop()
