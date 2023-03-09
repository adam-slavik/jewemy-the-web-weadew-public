from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/George_Washington"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the specific div element with the desired class
my_div = soup.find("a", class_="mw_parser_output")

# Find all the links in the paragraphs within that div
links = []
for p in my_div.find_all("p"):
    for a in p.find_all("a"):
        if a.has_attr("href"):
            links.append(a["href"])

print(links)