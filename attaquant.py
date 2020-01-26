import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1111))
s.listen(5)
client, infos = s.accept()

while True:
	try:
		send = input("> ").encode()
		client.send(send)
		recu = client.recv(1024)
		print(recu.decode())
	except KeyboardInterrupt:
		exit()
	except Exception as e:
		print(e)
