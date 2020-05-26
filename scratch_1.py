import time
from datetime import datetime
import requests
def block_website(website_block):
    pass

def site_avaliable(x):
   # response = requests.get("http://"+x)
    try :
        response = requests.get("http://" + x)
        if int(response.status_code)==200:
            website_block.append(site)

        else:
            print("Site is not reachable")
    except:
        print("Wrong value Try again")
def unblock_website(website):
    if website in website_block:
        website_block.remove(website)
    else:
        print("Wrong value")

website_block=[]
y="y"
while y=="y" or y=="yes":
    site=input("Enter website to Block: ")
    site_avaliable(site)
    y=input("Do you want block more website y or n? ")

#unblock_website(input("Do you want unblock any website? If yes then enter otherwise skip"))

print(website_block)