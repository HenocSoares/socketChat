import socket

#Socket creation
srvr_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to an addres + port set
host = "localhost"
port = 65000
srvr_socket.bind((host, port))

#List for incoming connections
srvr_socket.listen()

print(f"Server is listening on {host}:{port}")

#Accept and deal with incoming connections
while True:
	client_socket, client_address = srvr_socket.accept()
	print(f"Connection from {client_address} established.")

	try:	
		while True:
			message = client_socket.recv(1024)
			if not message:
				break
			print(f"Received from{client_address}: {message.decode()}")
				
			#Message back
			response = input("Enter a response: ")
			client_socket.send(response.encode())
	except (ConnectionResetError, socket.error, socket.timeout):
		print(f"Connection with {client_address} has been lost.")
	finally:	
		#Finalize client socket at all times
		client_socket.close()
