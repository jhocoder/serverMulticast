import socket, time, datetime

##Creamos socket Dtagram. Los multicast son UDP.
with socket.socket(socket.AF_INET,
                   socket.SOCK_DGRAM) as sock:

    sock.setsockopt(socket.IPPROTO_IP,
                    socket.IP_MULTICAST_TTL,
                    1)

    message = 'Hello World desde el PUBLISHER '

    multicast_group = ('224.3.29.71', 5557)

    print('Servidor iniciado...')

    while True:

##        sock.sendto(message.encode('utf-8'),
##                    multicast_group)
        for i in range(20):

            sock.sendto((message+str(i)+" "+str(datetime.datetime.now())).encode('utf-8'), multicast_group)
            time.sleep(1)






            





        







    
