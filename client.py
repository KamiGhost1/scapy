from scapy.all import *

secret_tos = 0xD
dest = '192.168.0.95'
text = '\1hello my friend!\0'

print(f"start sending to {dest}\nmsg: {text}")

i = 0
for char in text:
    ip = IP(tos=secret_tos, dst=dest, flags='DF')
    del ip.chksum
    ip.chksum = 256 * i + ord(char)
    send(ip)
    i+=1

print("done")