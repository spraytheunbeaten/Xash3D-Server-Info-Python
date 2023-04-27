#import

import socket
import os

#os

os.system("clear")

#input

print("----- Coded by SpRaY ----- \n")
print("Discord: ! SpRaY \n")

HOST = input("Sunucu IP adresi: ")
PORT = 27015

#socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = b"\xff\xff\xff\xffTSource"
s.sendto(message, (HOST, PORT))

#get info

try:
    data, addr = s.recvfrom(1024)
except KeyboardInterrupt:
    print("Program sonlandırıldı.")
else:
    print(data)

#end

s.close()