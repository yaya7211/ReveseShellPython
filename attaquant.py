import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1111))
s.listen(5)
client, infos = s.accept()

while True:
	try:
		cd = client.recv(10000000)
		send = input(cd.decode()+"> ")
		client.send(send.encode())
		recu = client.recv(10000000)
		print(recu.decode())
	except KeyboardInterrupt:
		exit()
	except Exception as e:
		print(e)
