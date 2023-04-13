#importy potrebných funkcií
from bs4 import BeautifulSoup
import re
import requests
# miesto pre zadanie linku
found = 0
linkss = []
site = "https://e.dennikn.sk/3302347/o-kolko-treba-znizit-hypoteku-aby-vam-nestupla-mesacna-splatka-kalkulacka/?ref=tit&_ga=2.10539188.1437119928.1680161329-727828214.1671089231"
# funkcia ako kód otvorí stránku ktorú cheme ohodnotiť
response = requests.get(site)

soup = BeautifulSoup(response.content, 'html.parser')
def class_name():
    if "dennik" in site:
        class_="a_single"

#hľadanie linku/preberanie medzi nimi
for div in soup.find_all('div', class_=class_name()):
    for d in div.find_all('li'):
        linkss.append(str(d))

# výpis všetkých linkov na stránke
print("Here are all the links on the site:")
print('\n'.join(linkss))
# výpis počtu linkov na stránke
for l in linkss:
    found += 1
print()
print("This is how many links are on the site:")
print(found)