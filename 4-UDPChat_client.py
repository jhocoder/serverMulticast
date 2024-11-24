import socket

HOST = 'localhost'
PORT = 65432

buffersize = 4096

c_sock = socket.socket(socket.AF_INET,
                       socket.SOCK_DGRAM)

while True:

    msg = input(">")
    c_sock.sendto(msg.encode('utf-8'), (HOST, PORT))
    data, addr = c_sock.recvfrom(buffersize)
    print("Mensaje del servidor ECHO:",
          data.decode('utf-8'))






    
