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
            x = 4
            # can be input to allow direct grab of a word
            # this takes a href link then splits it on ever / gets the 5 element 
            if y >= 4:
              brands = elements.split('/',5)[4]  
              # checks the brand name for .html extension, if it has it gets removed
              html = ".html"
              if html in brands:
                  brand = brands.split('.',1)[0] 
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
        finalList[i]= []
    return(finalList)


def href_To_Values(hrefList,finalList):
    # this gets all of the keys from the final list, uses those keys to check if there are any matches href list, if their are will assign those values to the correct key
    for items in finalList.keys():
        for elements in hrefList:
            if items in elements:
                finalList[items].append(element)
                


def main():
    x = 0
    finalList = {}
    url = 'https://beavertools.com/brands.html'
    hrefList = HrefList(url)
    word = 'brands'
    tableHeaders= table_Headers(hrefList,word)
    brandURL = brand_URL(hrefList,tableHeaders)
    listToKeys =list_To_Keys(tableHeaders,finalList)
    print(finalList)
    

    
    

    
    
   

    






if __name__ == "__main__":
    main()
