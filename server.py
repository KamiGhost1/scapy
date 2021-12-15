from scapy.all import *
import time
import base64

msg = ""
timeStart = 0
timeStop = 0
name = ""
base = False
isFile = False

def sniffer():
    sniff(
        filter='ip[1]=0xD',
        prn=lambda x: handler(x)
    )
    pass

def handler(x):
    global msg
    global timeStart
    global timeStop
    global base
    global isFile
    global name
    symbol = chr(x[IP].chksum % 256)
    if(symbol == '\1' or symbol == '\3'):
        if(symbol == '\3'):
            base = True
            isFile = True
        msg = ""
        print("### new msg started ###")
        timeStart = time.time()
    
    elif(symbol == '\2'):
        name = msg
        msg = ""
        return
    elif(symbol == '\0' ): 
        timeStop = time.time()
        if(timeStart > 0):
            isTime = timeStop-timeStart
            print(f"time is: {isTime}")
        if(not base):
            print(msg)
        else:
            msg = base64.b64decode(msg)
            print(f"file {name} is load")
            writer = open(name, "wb")
            writer.write(msg)
            writer.close()
            pass
        msg = ""
    else:
        msg += symbol
    pass

print("start sniffing")
sniffer()