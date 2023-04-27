import socket

import struct

import os

os.system('clear')

print("--------------------Xash3D Server Info--------------------")

ip = input("IP Adress: ")

port = int(input("Port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.settimeout(3.0)

s.connect((ip, port))

packet = b"\xFF\xFF\xFF\xFFTSource Engine Query\x00"

s.send(packet)

try:

    data, addr = s.recvfrom(4096)

except socket.timeout:

    print("Server did'nt response!")

    exit()

 #color by dumb3x

def remove_color_tags(text):

    colors = [

        "^0",

        "^1",

        "^2",

        "^3",

        "^4",

        "^5",

        "^6",

        "^7",            

        "^8",

        "^9"

    ] 

    

    for x in colors:

        text = text.replace(x, "")

    return text

header = struct.unpack("<4s", data[:4])[0]

if header == b"\xFF\xFF\xFF\xFF":

    data = data[4:]

    data_split = data.split(b"\x00")

    server_name = data_split[0].decode("utf-8")

    map_name = data_split[1].decode("utf-8")

    game_dir = data_split[2].decode("utf-8")

    game_desc = data_split[3].decode("utf-8")

    num_players = data[49]

    max_players = data[50]

    print("--------------------")

    print("Server Name: ", remove_color_tags(server_name))

    print("--------------------")

    print("Map: ", map_name)

    print("--------------------")

    print("Player Number: ", num_players, "/", max_players)

    print("--------------------")

else:

    print("ERROR!")

s.close()

