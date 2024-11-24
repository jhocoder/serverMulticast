import socket, struct

with socket.socket(socket.AF_INET,
                   socket.SOCK_DGRAM) as sock:

    server_address = ('', 5557)
    sock.bind(server_address)

    multicast_group = '224.3.29.71'

    group = socket.inet_aton(multicast_group)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP,
                    socket.IP_ADD_MEMBERSHIP,
                    mreq)

    while True:

        msg, server = sock.recvfrom(2048)

        print(str(server))
        print(msg.decode('utf-8'))









        









    









    

    
