import requests
import urllib
from bs4 import BeautifulSoup
import os
import exifread




url = "http://python.vic-tim.de/images/"
response = requests.get(url)

found_images = []
if response.status_code == 200:
    
    doc = BeautifulSoup(response.text, "html.parser")
    
    images = doc.find_all("img")
    
    for img in images:
        path = urllib.parse.urljoin(url, img.attrs["src"])
        found_images.append(path)


if not os.path.exists("./images"):
    os.mkdir("./images")


for found_image in found_images: 
    filename = found_image.split("/")[-1]
    
    response = requests.get(found_image)
    with open("./images/" + filename, "wb") as file:
        file.write(response.content)
    

with open("./images/img-1.jpg", "rb") as file:
    tags = exifread.process_file(file)
    for key, value in tags.items():
        print(str(key) + ": " + str(value))