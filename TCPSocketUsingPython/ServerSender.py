import socket
import tqdm
import os
import socket
import time



BUFFER_SIZE = 1024 # send 4096 bytes each time step
filename = "runtime.txt"
SEPARATOR = "<SEPARATOR>"
filesize = os.path.getsize(filename)
filesize = int(filesize)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 3389))
s.listen(5)


progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established.")
        clientsocket.send(f"{filename}{SEPARATOR}{filesize}".encode())
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                print("Break")
                break
            # print("sent")
            clientsocket.sendall(bytes_read)
            progress.update(len(bytes_read))
s.close()