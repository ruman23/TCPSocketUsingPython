import socket
import os
import time
import tqdm

HEADERSIZE = 10
BUFFER_SIZE = 1024
SEPARATOR = "<SEPARATOR>"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('35.203.25.23', 3389))

# s.send("Send me the file".encode())

received = s.recv(BUFFER_SIZE).decode()
print(received)
filename, filesize = received.split(SEPARATOR)
# remove absolute path if there is
filename = os.path.basename(filename)
# convert to integer
filesize = int(filesize)

progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

with open(filename, "wb") as f:
    while True:
        bytes_read = s.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        f.write(bytes_read)
        # print(len(bytes_read))
        # print(msg)
        progress.update(len(bytes_read))

s.close()