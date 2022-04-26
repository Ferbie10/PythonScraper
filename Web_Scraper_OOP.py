import requests
from bs4 import BeautifulSoup
from collections import Counter

class Web_Search:
    def __init__(self,URL):
        self.URL = URL

    def Web_list(self):
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

class Filter_By_Keyword():
    def __init__(self,keyWord,hrefList):
        self.hrefList = hrefList
          
        self.keyWord = keyWord
  
    def filterByKeyword(self):
        keywordListed = []
        for items in self.hrefList:

            if self.keyWord in items:
                keywordListed.append(items)
        return(keywordListed)


 
p = Web_Search('https://beavertools.com/brands/amana.html')
hrefList = p.Web_list()
keyWord = 'amana'
x = Filter_By_Keyword(keyWord,hrefList)

for items in x:

    websearch= Web_Search(items) 
