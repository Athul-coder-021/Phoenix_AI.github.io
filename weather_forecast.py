import requests
from bs4 import BeautifulSoup

search = "weather in jaipur"
URL = f"https://www.google.com/search?q={search}"

req = requests.get(URL)
sav = BeautifulSoup(req.text,"html.parser")
print(sav.text)
#update = sav.find("div",class_= "BNeawe").text()
#print(update)