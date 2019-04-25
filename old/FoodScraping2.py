from bs4 import BeautifulSoup

soup = BeautifulSoup(open(r"C:\Users\Alex\Desktop\Food\www.bbc.co.uk\food\recipes\aberdeenbutteriesrow_92370\shopping-list\\*"), "html.parser")

for ingredient in soup.find_all('label', {'class' : 'shopping-list__label'}):
    print(ingredient)