#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:58:16 2022

@author: dr404


"""


from termcolor import colored
import scapy.all as scapy
import argparse

def print_banner(title=""):
    
    
    print (colored('''
 ================================================================
#                                                                #
#      _   __     __     _____                                   #
#     / | / ___  / /_   / ___/_________ _____  ____  ___  _____  #
#    /  |/ / _ \/ __/   \__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/  #
#   / /|  /  __/ /_    ___/ / /__/ /_/ / / / / / / /  __/ /      #
#  /_/ |_/\___/\__/   /____/\___/\__,_/_/ /_/_/ /_/\___/_/       #
#                                               by Dr.404        #
#                                                                #
#                                 https://github.com/Dr-404      # 
#                                 Myanmar Pentester Community    #
#                                                                #
 ================================================================ 
''', 'green',attrs=(['bold'])))





def scan(ip):
    
    #  Creating ARP request to broadcast    
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # Creating Final Packet to Broad Cast    
    arp_request_broadcast = broadcast/arp_request
    
    # Sending Request(broadcast) and caputer request 
    # The request contain two list (asnwer, and unansewer)
    
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]    
  

   
    # Create Empty list to store data after looping answered list    
    client_list = []
    
    # Use For Loop to extract data from answer list    
    
    for element in answered_list:      
        
        
        source_ip = element[1].psrc
        source_mac = element[1].hwsrc
        
        # creating dictionary (only ip and mac address) using each data from answered list
        client_dict = {"ip":source_ip , "mac":source_mac}
        
        # adding data to client_list from client_dict (dictionary data)
        client_list.append(client_dict)
        
    return client_list        
        
        

def print_result(result_list):
    print("IP\t\t\tMac Address\n---------------------------------------")
    
    for client in result_list:
        print(client['ip']+"\t\t"+client['mac'])
    
    
def get_argument(): 
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help=("Target IP/Ip Range.")              )
    option = parser.parse_args()
    return option
        
        
def main(): 
    
    print_banner()


    options = get_argument()    
        
    scan_result= scan(options.target)
    print_result(scan_result)
    
    
    
    
if __name__=='__main__':
    main()
















