import socket
import os
import time

t1 = time.time()
print "t1 : ", t1
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.11"
port = 12345
s.connect((host, port))
s.send("PING\r")
str = s.recv(1024)
s.close()

t2 = time.time()
print "t2 : ", t2
strs = str.split(' ')
t3 = strs[1]
print "t3 : ", t3
rst = float(t3) - (t1+t2)/2
print "rst : ", rst

