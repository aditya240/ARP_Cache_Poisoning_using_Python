# ARP_Cache_Poisoning_using_Python

Overview

This Python script demonstrates how to perform ARP spoofing using the Scapy library. ARP spoofing is a type of attack in which an attacker sends falsified ARP (Address Resolution Protocol) messages over a local area network, resulting in the linking of an attacker's MAC address with the IP address of a legitimate computer or server on the network.

Requirements

Python 3.x
Scapy library: Can be installed using pip install scapy
Configuration

Before running the script, you need to replace the placeholder MAC and IP addresses with the actual addresses of the machines involved:

M01_MAC: MAC address of Machine 1 (the attacker's machine)
M02_IP: IP address of Machine 2 (the target machine)
M03_IP: IP address of Machine 3 (the machine whose identity is being spoofed)
E.dst: Destination MAC address (can be the MAC address of Machine 2 or the broadcast MAC address ff:ff:ff:ff:ff:ff)
How to Use

Update the script with the correct MAC and IP addresses.
Run the script from the command line:
python3 arp_spoofing.py

How it Works

The script creates an Ethernet frame and an ARP packet using Scapy.
The Ethernet frame's source MAC address is set to the attacker's MAC address, and the destination MAC address needs to be set to the target's MAC address or the broadcast MAC address.
The ARP packet's source and destination IP addresses are set to the IP addresses of the machine being impersonated and the target machine, respectively. The source MAC address is set to the attacker's MAC address.
The ARP packet is set to be an ARP Request (or ARP Reply if uncommented).
The ARP packet is attached to the Ethernet frame, and the combined packet is sent onto the network.
The ARP packet is printed to the console for debugging purposes using ls(A).
Security Implications

ARP spoofing can lead to man-in-the-middle attacks, denial of service attacks, and session hijacking.
This script is for educational purposes only and should not be used on any network or system without explicit permission.
Disclaimer

This script is provided for educational purposes only. Using this script for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. The author assumes no liability and is not responsible for any misuse or damage caused by this program.
