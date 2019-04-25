from bs4 import BeautifulSoup

soup = BeautifulSoup(r"C:\Users\Alex\Desktop\Food\www.bbc.co.uk\food\recipes\aberdeenbutteriesrow_92370\shopping-list\index", "html.parser")

print(soup)

for ingredient in soup.find('body'):
    print(ingredient)