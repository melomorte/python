#client
import socket
HOST = '127.0.0.1'
PORT = 4000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print('1 - para sair.\n')
msg = raw_input()
if msg == '1':
 	tcp.close()
