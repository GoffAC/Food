# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:49:09 2019

@author: Alex
https://stackoverflow.com/questions/43148784/local-html-file-scraping-urllib-and-beautifulsoup

"""

import os
from bs4 import BeautifulSoup 
phone = [] # A list to store all the phone
path=r"\Users\Alex\Desktop\www.bbc.co.uk\food\recipes"
# This is your folder name which stores all your html 
#be careful that you might need to put a full path such as C:\Users\Niche\Desktop\htmlfolder 
for filename in os.listdir(path): #Read files from your path
     #Here we are trying to find the full pathname
     for x in filename: #We will have A-H stored as path
           subpath = os.path.join(path, filename) 
           for filename in os.listdir(subpath):
           #Getting the full path of a particular html file
                fullpath = os.path.join(subpath, filename)
                #If we have html tag, then read it
                if fullpath.endswith('.html'): continue
                #Then we will run beautifulsoup to extract the contents
                soup = BeautifulSoup(open(fullpath), 'html.parser')
                    #Then run your code
                    # grabs each field
                #contactname = page_soup.findAll("td", {"itemprop": "name"})
                    
                    #Outputs as text without tags
                    #Company = contactname[0].text
                print (contactname)
                    
                    #Here you might want to consider using dictionary or a list
                    #For example append Phone to list call phone
                #phone.append(Phone)