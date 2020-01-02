#!/usr/bin/python3
import socket
import threading

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("0.0.0.0",8888))

server.listen()
conn,ip=server.accept()


def incoming():
	data=conn.recv(1024)
	while True:
		if data:
			if b"byebye" in data:
				conn.send(b"byebye")


			else:
				print("\nCLIENT: "+data.decode('utf-8').strip("\n"))
		data=conn.recv(1024)


def outgoing():
	while True:
        	msg=input("SERVER:")
        	conn.send(msg.encode())



thread1 = threading.Thread(target=incoming, )
thread2 = threading.Thread(target=outgoing, )

thread1.start()
thread2.start()
