import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1111))
s.listen(5)
client, infos = s.accept()
while True:
	a = client.recv(1024)
	a = a.decode()
	a = a+"> "
	send = input(a)
	client.send(send.encode())
	recu = client.recv(1024)
	print(recu.decode())