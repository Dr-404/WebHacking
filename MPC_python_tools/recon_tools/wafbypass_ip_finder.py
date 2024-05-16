
import requests
import colorama
from colorama import Fore, Style
import json
from termcolor import colored, cprint
import pyfiglet

#My Banner

banner = pyfiglet.figlet_format("Real IP Finder", font = "slant")
cprint(banner, 'green', attrs=['blink'])
cprint("                                                 by Dr.404\n",'green',attrs=['blink'])

# print()
# For colored Output

colorama.init(Style.BRIGHT)
blue = Fore.BLUE+Style.BRIGHT
green = Fore.GREEN+Style.BRIGHT
reset = Fore.RESET


# Requesting Input
cprint("Please edit the 'key' variable with your securityTrail API Key!!!! \n",'blue')
domain = str(input("Enter your domain : "))
print()

# PLease type your API key in Key parameter
key = "6jWeKbd49Q1cEvwp0Ri5TyWsyD3ttkce" # Edit this with your API key


# Requesting API json Data

url = "https://api.securitytrails.com/v1/history/"+domain+"/dns/a"
headers = {

    "Accept": "application/json",

    "APIKEY": key

}
response = requests.get(url, headers=headers)
response_json = response.json()

responseData = response_json["records"]

for data in responseData:
    try:
        ip = data['values'][0]['ip']
        org = data['organizations'][0]
        date = data['last_seen']
        if org == "Cloudflare, Inc.":
            pass
        else:
            print("The Real IP of Domain may be : ",blue+ip+reset)
            print("The Organization of Domain Hosted is : ",blue+org+reset)
            print("This IP is Last seen on : ",blue+ date +reset)
            print()
    except: IndexError
