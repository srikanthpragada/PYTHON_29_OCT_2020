import requests
from bs4 import BeautifulSoup
import datetime

resp = requests.get(f"http://www.srikanthtechnologies.com/rss.xml")
bs = BeautifulSoup(resp.text, 'lxml-xml')
items = bs.find_all("item")
for item in items:
    title = item.find("title").text
    link = item.find("link").text
    pubdate_str = item.find("pubDate").text
    try:
        pubdate = datetime.datetime.strptime(pubdate_str[5:16], "%d %b %Y")
        if (datetime.datetime.today() - pubdate).days <= 100:
            print(title.strip())
            print(link)
            print(pubdate_str)
            print('-' * 80)
    except:
        pass
