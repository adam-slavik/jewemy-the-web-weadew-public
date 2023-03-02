import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/George_Washington"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

paragraph = soup.find("div", class_="mw-parser-output").find("p")

print(paragraph.text

separare code ==>
from bs4 import BeautifulSoup
import requests

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the specific div element with the desired class
my_div = soup.find("div", class_="my_class")

# Find all the links in the paragraphs within that div
links = []
for p in my_div.find_all("p"):
    for a in p.find_all("a"):
        if a.has_attr("href"):
            links.append(a["href"])

print(links)