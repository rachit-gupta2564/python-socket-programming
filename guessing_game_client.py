import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (socket.gethostname(), 1234)
s.connect(address)
while True:
    guess = input("Enter your guess (between 1 and 100): ")
    s.send(guess.encode())
    response = s.recv(1024).decode()
    print(response)
    if response == "Correct! You guessed it right.":
        break
s.close()