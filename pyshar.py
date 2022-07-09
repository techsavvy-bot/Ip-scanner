from dis import dis
from traceback import print_tb
import pyshark
from pprint import pprint

textfile = open('ip_complete.csv','r')
data = textfile.read().splitlines()
print(data[3])
print("Program is running")

capture = pyshark.LiveCapture(interface='wlp0s20f3')
for packet in capture.sniff_continuously():
        try:
            protocol = packet.transport_layer   # protocol type
            src_addr = packet.ip.src            # source address
            src_port = packet[protocol].srcport   # source port
            dst_addr = packet.ip.dst            # destination address
            dst_port = packet[protocol].dstport   # destination port

                # output packet info
            # print (dst_addr, protocol)
            if(dst_addr in data):
                print("Not safe",packet)
            # print("this is one packet****************************")
        except AttributeError as e:
        # ignore packets other than TCP, UDP and IPv4
            pass