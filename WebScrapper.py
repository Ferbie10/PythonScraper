import os
import requests
from bs4 import BeautifulSoup, element
import csv
from collections import Counter


def HrefList(url):
    URL = url
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    source=requests.get(URL, headers=headers)
    soup = BeautifulSoup(source.text, "html.parser")
    hrefList = []
    for i in soup.findAll('a', href=True):
        # find all href on html web page
        test = (i['href'])
        # add all href to hrefList
        hrefList.append(test)
    

    return(hrefList)


def table_Headers(hrefList,word):
    tableHeaders = []

    for elements in hrefList:
        if word in elements:
            counter = Counter(elements)
            y= int(counter['/'])
            # can be input to allow direct grab of a word
            # this takes a href link then splits it on ever / gets the 5 element 
            if y >= 4:
              brands = elements.split('/',5)[4]  
              # checks the brand name for .html extension, if it has it gets removed
              html = ".html"
              if html in brands:
                  brand = brands.split('.',1)[0]
                  x = int(counter['-'])
                  if x >= 3:
                      brand = brand.split('-',4)[3]
                      if brand not in tableHeaders:
                          tableHeaders.append(brand)
                  else:
                      if brand not in tableHeaders:
                          tableHeaders.append(brand)
                   


    return(tableHeaders)


def brand_URL(hrefList,tableHeaders):
    #takes the brand names from table Headers. Adds the .html extension and check href list to grab the main brand webpage
    brandURL = []
    for element in tableHeaders:
        brandhtml = element+'.html'
        for elements in hrefList:
            if brandhtml in elements:
                if elements not in brandURL:
                    brandURL.append(elements)

    return(brandURL)
                    
def list_To_Keys(tableHeaders,finalList):
    #takes on teh brand names assigns them to keys in a directory
    for i in tableHeaders:
        # takes each of the brand names and added them to a key in the directory
        finalList[i]= []
    return(finalList)


def href_To_Values(hrefList,finalList):
    # this gets all of the keys from the final list, uses those keys to check if there are any matches href list, if their are will assign those values to the correct key
    for items in finalList.keys():
        # Gets all keys/brand names from final list and stores in Var Items
        for elements in hrefList:
            #Gets all href from list and assigns them to element

            if items in elements:
                # Check each href link to see if one it contains one of the brand names
                if elements not in finalList[items]:
                    # Checks to see if the href link as already been added to the final list dir
                    finalList[items].append(elements)

    return(finalList)




def main():
    
    finalList = {}
    url = 'https://beavertools.com/brands/amana.html'
    hrefList = HrefList(url)
    word = 'brands'
    tableHeaders= table_Headers(hrefList,word)
    brandURL = brand_URL(hrefList,tableHeaders)
    listToKeys =list_To_Keys(tableHeaders,finalList)
    hrefToValues = href_To_Values(hrefList,finalList)
    brandItems = brand_Items(brandURL,tableHeaders)
    with open('Brands.txt','w')as f:

        for key,value in finalList.items():
            for v in value:
                lines=(key+ ': '+v)
                f.write(lines)
                f.write('\n')
        
    

 

if __name__ == "__main__":
    main()
    
    

    
    
   

    






if __name__ == "__main__":
    main()
