import requests
host_path="/etc/hosts"
def block_website(website_block):
    global host
    redirect="127.0.0.1"
    with open(host_path,'r+') as file:
        content=file.read()
        for website in website_block:
            if website in content:
                print("It is already blocked")
                pass
            else:
                file.write(redirect+" "+website+"\n")
        print(content)
def site_avaliable(x):
    try :
        response = requests.get("http://" + x)
        if int(response.status_code)==200:
            website_block.append(site)
        else:
            print("Site is not reachable")
    except:
        print("Wrong value Try again")
def unblock_website(website):
    global host_path

    with open(host_path,'r') as file:
        content = file.readlines()
        #if ("127.0.0.1 "+website) not in content:
         #   print("This website is not blocked")
    with open(host_path,'w') as file:
        for line in content:
            if line.strip("\n") != ("127.0.0.1 "+website):
                file.write(line)
website_block=[]
y="y"
while y=="y" or y=="yes":
    site=input("Enter website to Block: ")
    site_avaliable(site)
    y=input("Do you want block more website y or n? ")
print(website_block)
block_website(website_block)
while True:
    z=(input("Do you want unblock any website? If yes then enter otherwise skip"))
    unblock_website(z)
    if z=='n':
        break