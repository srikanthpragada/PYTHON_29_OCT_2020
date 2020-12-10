import requests
from bs4 import BeautifulSoup

resp = requests.get(f"https://www.w3schools.com/")
bs = BeautifulSoup(resp.text, 'html.parser')

for link in bs.find_all("a"):
    href = link['href']
    if not href.startswith("javascript"):
        print(href)
