import socket

HOST = 'localhost'
PORT = 65432
buffersize = 4096

s_sock = socket.socket(socket.AF_INET,
                       socket.SOCK_DGRAM)

s_sock.bind((HOST, PORT))

while True:
    
    print("Escuchando peticiones desde", s_sock.getsockname())
    data, addr = s_sock.recvfrom(buffersize)
    print("Mensaje del cliente:", data.decode('utf-8'))

    
    s_sock.sendto(data, addr)





    






