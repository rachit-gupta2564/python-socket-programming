import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 1234)
s.connect(address)

data = input('Client: ').encode()
s.send(data)
res = s.recv(1024)
print('Server: ',res.decode())
s.close()