import os
import requests

#get domains using subfinder into subdomains.txt

op1 = input("1. Single domain\n2. Domains file\nEnter option: ")
if op1 == "1" or op1 == "input":
    domain = input("Enter domain: ")
    os.system(f"subfinder -d {domain} -o subdomains.txt --silent")
if op1 == "2" or op1 == "file":
    domain = input("Enter domains file: ")
    os.system(f"subfinder -dL {domain} -o subdomains.txt --silent")
else:
    print("Error")

domains = []
with open("subdomains.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        domains.append(line)

op2 = input("Want status codes in a file? (y/n): ")
if op2 == "y":
    file = input("Enter file name: ")
    with open(file, "w") as f:
        for domain in domains:
            try:
                domain = domain.replace("\n", "")
                r = requests.get(f"https://{domain}")
                f.write(f"{domain} - {r.status_code}\n")
            except:
                pass
elif op2 == "n":
    for domain in domains:
        try:
            domain = domain.replace("\n", "")
            r = requests.get(f"https://{domain}")
            print(f"{domain} - {r.status_code}\n")
        except:
            pass
