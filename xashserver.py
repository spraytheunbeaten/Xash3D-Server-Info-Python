#import
import socket
import os

#os
os.system("clear")

print("""
----- Coded by SpRaY -----
Discord: ! SpRaY
""")

#input
ip = input("Sunucu IP adresi: ")
port = input("Sunucu Portu: ")

addr = (ip, int(port))

#socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

packet = b"\xff\xff\xff\xffTSource"

#get info
try:
    sock.sendto(packet, addr)
    data = sock.recvfrom(1024)
    print(data)
except Exception as err:
    print(f"Program sonlandırıldı.\n {err}")

sock.close()
