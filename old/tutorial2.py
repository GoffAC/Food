from bs4 import BeautifulSoup

f = open("test.html")      # simplified for the example (no urllib)
soup = BeautifulSoup(f)
f.close()

receipe = soup.findAll("h1", {"class": "content-title__text"})

print (receipe[0].text) 

ingredients = soup.findAll("label", {"class": "shopping-list__label"})
for ingredient in ingredients:
    ingData = ' '.join(ingredient.text.split())
    print (ingData)    

# listItems = []

# for ingredient in ingredients:
#     listItems = listItems + ingredient[0].text

# print (listItems)    
    

# title = titleLst[0].contents[0]
# print title                # the string from the h1 element

# g_a = soup.findAll("div", {"id" : "a"})  # the elements from inside the div a element
# alst = []                                # the future result list
# for x in g_a:
#     for elem in x.findAll('div'):        # the divs inside the div a
#         print elem.contents              # just to see what is inside
#         alst.append(elem.contents[0].strip('\n\t ,'))  # collect the wanted info
        
# print alst               # wanted result in a technical form            
# print ', '.join(alst)    # wanted result as a string (items separated by comma and space