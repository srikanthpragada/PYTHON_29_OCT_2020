from bs4 import BeautifulSoup

with open("products.xml", "rt") as f:
    bs = BeautifulSoup(f, 'lxml-xml')
    products = bs.find_all("product")
    for product in products:
        name = product.find("name").text
        price = int(product.find("price").text)
        print(f"{name:30} {price:10}")
