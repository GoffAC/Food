from bs4 import BeautifulSoup
import glob
import os
import re
import contextlib


@contextlib.contextmanager
def stdout2file(fname):
    import sys
    f = open(fname, 'w')
    sys.stdout = f
    yield
    sys.stdout = sys.__stdout__
    f.close()


def trade_spider():
    import json
    data = {}

    os.chdir(r"C:\Users\Alex\Desktop\Food\www.bbc.co.uk\food\recipes")
    for file in glob.iglob('**/*.html', recursive=True):
        with open(file, encoding="utf8") as f:
            contents = f.read()
            soup = BeautifulSoup(contents, "html.parser")
            for item in soup.findAll("h1", {"class": "content-title__text"}):
                data[item.text] = []
                # print('\n\r')
                # print (item.text)
                ingredients = soup.findAll("label", {"class": "shopping-list__label"})
                for ingredient in ingredients:
                    ingData = ' '.join(ingredient.text.split())
                    data[item.text].append(ingData)
                    # print (ingData)    
    with open('data.text','w') as outfile:
        json.dump(data, outfile)
          
trade_spider()