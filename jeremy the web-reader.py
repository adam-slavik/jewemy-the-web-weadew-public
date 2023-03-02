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

#importy potrebných funkcií
from bs4 import BeautifulSoup
import re
import requests
# miesto pre zadanie linku
found = 0
linkss = []
site = "https://en.wikipedia.org/wiki/George_Washington"
# funkcia ako kód otvorí stránku ktorú cheme ohodnotiť
response = requests.get(site)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

#hľadanie linku/preberanie medzi nimi
my_div = soup.find("div", class_="mw-parser-output")
links = my_div.find_all("a", href=re.compile("http"))

#links =  soup.find_all( "div", class_= "a_single", href = re.recompile ("http"))
for link in links:
    site = link.get ("href")
    if ".sk" in str(link) and  "autor" in str(link) and "?ref=" not in str(link) and "napunk" not in str(link) and "obchod" not in str(link) \
            and "predplatne" not in str(link) and "tema" not in str(link) :
        linkss.append(link.get('href'))
print()
# výpis všetkých linkov na stránke
print("Here are all the links on the site:")
print(linkss)
# výpis počtu linkov na stránke
for l in linkss:
    found += 1
print()
print("This is how many links are on the site:")
print(found)

# prototyp class hľadacieho sytému
class_names = {
    "dennikn": "a_single",
    "hlavnespravy": "menoclassy"}
