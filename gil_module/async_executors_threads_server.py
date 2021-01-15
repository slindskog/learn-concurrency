import time
import socket
import random
import asyncio
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

requests = 0


async def find_nth_prime(nth_prime):
    i = 2
    nth = 0
    last_prime = None
    while nth != nth_prime:
        if is_prime(i) == True:
            nth += 1
            last_prime = i
        i += 1
    return last_prime


def is_prime(num):
    if num == 2 or num == 3:
        return True
    div = 2
    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1
    return True


def monitor_requests_per_thread():
    global requests
    while True:
        time.sleep(1)
        print(f"{requests} requests/min", flush=True)
        requests = 0


class PrimeService:

    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port
        self.executor = ThreadPoolExecutor()

    async def handle_client(self, reader, writer):
        global requests
        while True:
            data = (await reader.read(4096)).decode()
            nth_prime = int(data)

            current_loop = asyncio.get_event_loop()
            prime = await current_loop.run_in_executor(self.executor, find_nth_prime, nth_prime)

            writer.write(str(prime).encode())
            await writer.drain()
            requests += 1


def run_simple_client(server_host, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((server_host, server_port))
    while True:
        server_socket.send("1".encode())
        server_socket.recv(4096).decode()


def run_long_request(server_host, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((server_host, server_port))
    while True:
        server_socket.send("100000".encode())
        server_socket.recv(4096)


async def main():
    server = PrimeService(server_host, server_port)
    await asyncio.start_server(server.handle_client, "127.0.0.1", server_port, )


def server_code():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.ensure_future(main())
    loop.run_forever()


if __name__ == "__main__":
    server_port = random.randint(10000, 65000)
    server_host = "127.0.0.1"
    Thread(target=server_code, daemon=True).start()

    time.sleep(0.1)

    Thread(target=monitor_requests_per_thread, daemon=True).start()
    Thread(target=run_simple_client, args=(server_host, server_port), daemon=True).start()

    time.sleep(2)

    Thread(target=run_long_request, args=(server_host, server_port), daemon=True).start()

    time.sleep(10)
