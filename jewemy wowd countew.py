import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# get the URL of the website
url = input("Enter the URL of the website: ")

# send a GET request to the website and get its HTML content
response = requests.get(url)
html_content = response.text

# create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# extract the text from the HTML content
text = soup.get_text()

# count the number of words in the text
word_count = len(text.split())

# get all the links in the website
links = soup.find_all('a')

# find the external links and put them in a list
external_links = []
for link in links:
    href = link.get('href')
    if href is not None and urlparse(href).netloc != urlparse(url).netloc:
        external_links.append(href)

# print the external links
if len(external_links) > 0:
    print("The website has", len(external_links), "external links:")
    print(external_links)
else:
    print("The website has no external links.")

# print the word count
print("The website has", word_count, "words.")
