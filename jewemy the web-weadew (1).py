# import re
# import requests
# from urllib import parse, request
# from bs4 import BeautifulSoup
# 
# URL = "https://bilgym.sk"
# page = requests.get(URL)
# found=0
# 
# # site =input("Enter a link: ")
# # r = request.urlopen(site)
# 
# # soup = BeautifulSoup(r.read(), 'html.parser')
# # for soup_li in soup.find_all(attrs={"class":'MainPageBG mp-box'}, href=re.compile("http")):
# #     if len(list(soup_li.children)) == 1 and soup_li.a:
# #         print (soup_li.a["href"])
# site =input("Enter a link: ")
# r = request.urlopen(site)
# 
# def get_links(root, html):
#     soup = BeautifulSoup(html, "html.parser")
#     for link in soup.find_all(attrs={"class":"top-item-wrapper-text"}, href=re.compile("http")):
#         for link in soup.find_all('a'):
#             href = link.get("href")
#             if href:
#                 text = link.string
#                 if not text:
#                     text = ""
#                     text = re.sub("\s+", " ", text).strip()
#                 yield (parse.urljoin(root, link.get("href")), text)
# 
# site =input("Enter a link: ")
# r = request.urlopen(site)
# print("Here are all links on the site:" )
# for l in get_links(site, r.read()):
#     print(l)
#     found += 1
#
# print("Here is the total number of links on the site:")
# print(found)
# #
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

found = 0
site = input("Pwease put you big link in me uwu:")
req = Request(site)
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll( "a", href=re.compile("http")):
    if ".sk" in str(link) and "?ref=" not in str(link) and "napunk" not in str(link) and "obchod" not in str(link) and "predplatne" not in str(link) and "tema" not in str(link) :
        links.append(link.get('href'))
print()
print("Hewe is ewewithing i found fow u daddy:")
print(links)

for l in links:
    found += 1

print()
print("This is how many i found fow u uwu:")
print(found)

class_names = {
    "dennikn": "a_single",
    "hlavnespravy": "menoclassy"}

# attrs = {"class": "mw-parser-output"})

import requests
from bs4 import BeautifulSoup
import urllib.parse

def scrape_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = []
    for article in soup.find_all(class_="article"):
        articles.append(article.text)
    return articles

def determine_validity(url):
    parsed_url = urllib.parse.urlparse(url)
    scraped_links = [link for link in scrape_links(url) if urllib.parse.urlparse(link).netloc != parsed_url.netloc]
    scraped_links = [link for link in scraped_links if "ad" not in urllib.parse.urlparse(link).netloc]
    num_links = len(scraped_links)
    if num_links > 100:
        return "This site is likely to be valid."
    elif num_links > 50:
        return "This site may be valid."
    else:
        return "This site may not be valid."

url = input("Enter a website to check for validity: ")
articles = scrape_articles(url)
if articles:
    print("The site has articles.")
else:
    print("The site does not have articles.")
print(determine_validity(url))
