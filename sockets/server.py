import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1234))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
data = conn.recv(1024)
response_data = str(int(data)**2)
conn.sendall(response_data)
conn.close()
