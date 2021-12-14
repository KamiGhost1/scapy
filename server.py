from scapy.all import *

msg = ""

def sniffer():
    sniff(
        filter='ip[1]=0xD',
        prn=lambda x: handler(x)
    )
    pass

def handler(x):
    global msg
    symbol = chr(x[IP].chksum % 256)
    if(symbol != '\0' ):
        msg += symbol
    else:
        print(msg)
        msg = ""
    pass

print("start sniffing")
sniffer()