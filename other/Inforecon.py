import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + "<url>")
    sys.exit(1)


req = requests.get("https://"+sys.argv[1])
print("\n"+str(req.headers))

gethostby  = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of " + sys.argv[1]+" is: " + gethostby + "\n")


req_two = requests.get("https://ipinfo.io/"+gethostby+"/json")
resp = json.loads(req_two.text)


print("Location: "+ resp["loc"])
print("Region: " + resp["region"])
print("City: " + resp["city"])
print("County: " + resp["country"])





