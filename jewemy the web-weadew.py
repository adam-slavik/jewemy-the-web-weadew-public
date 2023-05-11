#importy potrebných funkcií
from bs4 import BeautifulSoup
import re
import requests
from collections import Counter
from string import punctuation

# miesto pre zadanie linku
found = 0
linkss = []
site = "https://en.wikipedia.org/wiki/George_Washington"
# funkcia ako kód otvorí stránku ktorú cheme ohodnotiť
response = requests.get(site)

soup = BeautifulSoup(response.content, 'html.parser')
# def class_name():
#     if "dennik" in site:
#         class_="a_single"

#hľadanie linku/preberanie medzi nimi
for div in soup.find_all('div', class_="mw-references-wrap mw-references-columns"):
    for li in div.find_all('li'):
        link = li.find('a')['href']
        linkss.append(link)

# výpis všetkých linkov na stránke
print("Here are all the links on the site:")
print(', '.join(linkss))
# výpis počtu linkov na stránke
for l in linkss:
    found += 1
print()
print("This is how many links are on the site:")
print(found)

output_text = ""
for div in soup.find_all('div', class_="mw-parser-output"):
    output_text += div.get_text()

word_count = len(re.findall(r'\b\w+\b', output_text))
print()
print("Počet slov:")
print(word_count)

Credibitlity=found/word_count

print(Credibitlity)