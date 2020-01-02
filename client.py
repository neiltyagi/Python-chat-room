#!/usr/bin/python3
import socket
import threading

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=input("enter ip of server=")
client.connect((ip,8888))

def outgoing():
	while True:
		msg=input("CLIENT:")
		client.send(msg.encode())


def incoming():
	data=client.recv(1024)
	while True:
		if data:
			if b"byebye" in data:
				try:
					exit()
					sys.exit()
				except:
					print("press enter to exit")
			else:
                        	print("\nSERVER: "+data.decode('utf-8').strip("\n"))
		data=client.recv(1024)


thread1 = threading.Thread(target=incoming, )
thread2 = threading.Thread(target=outgoing, )

thread1.start()
thread2.start()

