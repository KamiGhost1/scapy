from logging import fatal
from scapy.all import *
import argparse
import base64

def formatMsg(data):
    return "\1"+data+"\0"

def formatMsgBase64(data):
    return "\3"+data+"\0"

def formatMsgBase64File(data, name):
    return "\3"+f"{name}\2"+ data +"\0"


def sendStegano(mode, path):
    secret_tos = 0xD
    dest = '192.168.0.95'
    text = '\1hello my friend!\0'
    i = 0
    ip = IP(tos=secret_tos, dst=dest, flags='DF')
    if(mode == False):
        pass
    if(mode == False and path!=False):
        text = formatMsg(path)
        pass
    if(mode == True and path != False):
        file = open(path, "rb")
        text = file.read()
        file.close()
        text = base64.b64encode(text)
        text = bytes.decode(text)
        text = formatMsgBase64File(text, path)     
        # print(text)   
        # return
    print(f"start sending to {dest}\nmsg: {text}")
    for char in text:
        # del ip.chksum
        ip.chksum = ord(char)
        send(ip, verbose=False)
        i+=1

    print("done")
    pass


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-f',type=str, help="path to file")
    parser.add_argument ('-m',type=str, help="message")
    return parser

parser = createParser()
namespace = parser.parse_args()

if(namespace.f):
    # print(namespace.f)
    sendStegano(True, namespace.f)
    pass
elif (namespace.m):
    sendStegano(False, namespace.m)
    pass
else:
    sendStegano(False, False)

