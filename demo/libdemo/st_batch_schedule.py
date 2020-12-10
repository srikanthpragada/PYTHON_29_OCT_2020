import requests
from bs4 import BeautifulSoup
import datetime

resp = requests.get(f"http://www.srikanthtechnologies.com/")
bs = BeautifulSoup(resp.text, 'html.parser')
table = bs.find(id='ctl00_ContentPlaceHolder1_GridView2')
rows = table.find_all("tr")[1:]
for row in rows:
    columns = row.find_all("td")
    year = datetime.date.today().year
    stdate = datetime.datetime.strptime(columns[2].text + "-" + str(year), "%d-%b-%Y")
    days = (stdate - datetime.datetime.today()).days
    if days >= 0:
        print(f"{columns[0].text:50} {columns[1].text:15} {stdate.strftime('%d-%b-%Y'):10} {days:2} days to go")
