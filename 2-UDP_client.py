import socket

HOST = 'localhost'
PORT = 65432

c_sock = socket.socket(socket.AF_INET,
                       socket.SOCK_DGRAM)

msg = "Soy un cliente UDP y lanzo un mensaje al servidor"

c_sock.sendto(msg.encode(), (HOST, PORT))

data, addr = c_sock.recvfrom(4096)

print("Mensaje desde el servidor:", data.decode())

c_sock.close()














