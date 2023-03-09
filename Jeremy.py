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

soup = BeautifulSoup(response.content, 'html.parser')

#hľadanie linku/preberanie medzi nimi
for div in soup.find_all('div', class_='mw-parser-output'):
    for link in div.find_all('a', href=True):
        href = link['href']
        # Prepend the protocol and domain to the relative URLs
        if href.startswith('/'):
            href = 'https://en.wikipedia.org' + href
            if "wikipedia" not in href or "#" not in href and href not in linkss:
                linkss.append(href)
# výpis všetkých linkov na stránke
print("Here are all the links on the site:")
print('\n'.join(linkss))
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