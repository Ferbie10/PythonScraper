import requests
from bs4 import BeautifulSoup
from collections import Counter
import os

class Web_Search:

    def __init__(self,URL):
        self.URL = URL
    def webSeach(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        source=requests.get(self.URL, headers=headers)
        soup = BeautifulSoup(source.text, "html.parser")
        hrefList = []
        for i in soup.findAll('a', href=True):
        # find all href on html web page
            test = (i['href'])
        # add all href to hrefList
            hrefList.append(test)
        return(hrefList)

class Web_Drill:
    def __init__(self,hrefList):
        self.hrefList = hrefList

    def webDrill(self):
        for items in self.hrefList:
            item = str(items)
            hrefLists = []
            substring = 'beavertools'
            if substring in item:
                try:
                    url = Web_Search(item)
                    hrefLists = url.webSeach()
                    for i in hrefLists:
                        if i not in hrefLists:
                           hrefLists.append(i)
                except:
                    print(item)
                            
        return(hrefLists)




def main():
    userURL = 'https://beavertools.com/'
    try:
        url = Web_Search(userURL)
        hrefList = url.webSeach()
    except:
        print('You have entered an invaild URL. Please try again:')
    url1 = Web_Drill(hrefList)
    hrefLists = url1.webDrill()
    print(len(hrefList))
    print(len(hrefLists))
   

main()