#server
import socket
HOST = ''
PORT = 4000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
	con, client = tcp.accept()
	print('conected: ', client)
	while True:
		msg = con.recv(1024)
		if not msg: break
		print(cliente, msg)
	print('desconnect...', client)
	con.close
