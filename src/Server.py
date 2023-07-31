import socket
from tqdm import tqdm


class Server:
    def __init__(self, port):
        ip = socket.gethostbyname(socket.gethostname())
        self.address = (ip, port)
        self.format = 'utf-8'
        self.size = 1024

    def server(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(self.address)
        sock.listen()

        print("[+] Listening...")

        """ Accepting the connection from the client. """
        conn, addr = sock.accept()
        print(f"[+] Client connected from {addr[0]}:{addr[1]}")

        """ Receiving the filename and filesize from the client. """
        data = conn.recv(self.size).decode(self.format)
        item = data.split("_")
        filename = item[0]
        filesize = int(item[1])

        print("[+] Filename and filesize received from the client.")
        conn.send("Filename and filesize received".encode(self.format))

        """ Data transfer """
        bar = tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=self.size)

        with open(f"recv_{filename}", "w") as f:
            while True:
                data = conn.recv(self.size).decode(self.format)

                if not data:
                    break

                f.write(data)
                conn.send("Data received.".encode(self.format))

                bar.update(len(data))

        """ Closing connection. """
        conn.close()
        sock.close()


if __name__ == '__main__':
    pass

