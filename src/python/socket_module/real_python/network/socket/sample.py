import socket
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(s)

server = 'pythonprogramming.net'
port = 80

server_ip = socket.gethostbyname(server)

print("104.237.143.20")
print (server_ip,"\n")

request = "GET /HTTP/ 1.1\nHost: "+server+"\n\n"

s.connect((server, port))
s.send(request.encode())
result = s.recv(4096)

#print ("result:",result)

while (len(result) > 0):
    print (result)
    result = s.recv(1024)
    sleep(1.0) 