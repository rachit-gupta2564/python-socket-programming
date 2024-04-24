import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (socket.gethostname(), 1234)
s.bind(address)
s.listen(1)
print("Waiting for connection...", address)
client, addr = s.accept()
print("Connections established", addr)
while 1:
    data = client.recv(1024)
    if not data:
        break
    print("Client:", data)
    data = input('Server:').encode()
    client.send(data)

client.close()
s.close()