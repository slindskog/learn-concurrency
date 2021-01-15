import time
import socket
import random
from threading import Thread


class PrimeService:

    def __init__(self, server_port):
        self.server_port = server_port

    def find_nth_prime(self, nth_prime):
        i = 2
        nth = 0
        last_prime = None
        while nth != nth_prime:
            if self.is_prime(i) == True:
                nth += 1
                last_prime = i
            i += 1
        return last_prime

    def is_prime(self, num):
        if num == 2 or num == 3:
            return True
        div = 2
        while div <= num / 2:
            if num % div == 0:
                return False
            div += 1
        return True

    def run_service(self):
        s = socket.socket()
        s.bind(('', self.server_port))

        # Put the socket into listening mode
        s.listen(5)
        client_socket, addr = s.accept()
        data = client_socket.recv(4096).decode()
        nth_prime = int(data)
        print(f"Asked to find the {nth_prime}-th prime")
        prime = self.find_nth_prime(nth_prime)
        client_socket.send(str(prime).encode())


def run_client(server_host, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((server_host, server_port))
    server_socket.send("7".encode())
    result = server_socket.recv(4096).decode()
    print(f"Prime found to be: {result}")


if __name__ == '__main__':
    server_port = random.randint(10000, 65000)
    server_host = '127.0.0.1'
    server = PrimeService(server_port)

    server_thread = Thread(target=server.run_service, daemon=True)
    server_thread.start()

    run_client(server_host, server_port)

    time.sleep(10)
