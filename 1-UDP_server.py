import socket

HOST = 'localhost'
PORT = 65432

buffersize = 4096

s_sock = socket.socket(socket.AF_INET,
                       socket.SOCK_DGRAM)

s_sock.bind((HOST, PORT))
print('Server UDP up...')

while True:

    data, addr = s_sock.recvfrom(buffersize)
    print('Mensaje del cliente:', data.decode(),
          'enviado por', addr)

    msg = "Hola soy un servidor UDP y te tiro el \
paquete a la cara"

    s_sock.sendto(msg.encode(), addr)










    






