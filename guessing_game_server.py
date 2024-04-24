import socket
import random
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (socket.gethostname(), 1234)
s.bind(address)
s.listen(1)
print("Waiting for connection...", address)
client, addr = s.accept()
print("Connection Established:", addr)
number = random.randint(1, 100)
print("Number to guess:", number)
while True:
    data = client.recv(1024).decode()
    if not data:
        break
    guess = int(data)
    print("Received guess:", guess)
    if guess == number:
        client.send("Correct! You guessed it right.".encode())
        break
    elif guess < number:
        client.send("Higher".encode())
    else:
        client.send("Lower".encode())
client.close()
s.close()