import socket

#Socket creation
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to the server
host = "localhost"
port = 65000
client_socket.connect((host, port))

#Communicate to the server (send)
while True:
	message = input("Enter a message (or ':exit' to quit): ")
	if message.lower() == ':exit':
		break
	client_socket.send(message.encode())
	
	#Receive the echo and print it
	response = client_socket.recv(1024)
	print("Server:", response.decode())
#Finalize socket (client)
client_socket.close()
