import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://en.wikipedia.org/wiki/George_Washington'

# Send a GET request to the URL
response = requests.get(url)

# Create a list for the links to stay in before being printed
links=[]

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the div with the 'mw-parser-output' class and loop through its links
for div in soup.find_all('div', class_='mw-parser-output'):
    for link in div.find_all('a', href=True):
        href = link['href']
        # Prepend the protocol and domain to the relative URLs
        if href.startswith('/'):
            href = 'https://en.wikipedia.org' + href
            if "wikipedia" not in href or "#" not in href and href not in links:
                links.append(href)

print(links)
