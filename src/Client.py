import os
import socket
import tqdm


class Client:
    def __init__(self, ip, port):
        self.address = (ip, port)
        self.format = 'utf-8'
        self.size = 1024

    def client(self, filename, filesize):
        """ TCP socket and connecting to the server """
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.connect(self.address)

        """ Sending the filename and filesize to the server. """
        data = f"{filesize}_{filesize}"
        soc.send(data.encode(self.format))
        msg = soc.recv(self.size).decode(self.format)
        print(f"SERVER: {msg}")

        """ Data transfer. """
        bar = tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=self.size)


        with open(filename, "r") as f:
            while True:
                data = f.read(self.size)

                if not data:
                    break

                soc.send(data.encode(self.format))
                msg = soc.recv(self.size).decode(self.format)

                bar.update(len(data))

        """ Closing the connection """
        soc.close()


if __name__ == '__main__':
    pass
