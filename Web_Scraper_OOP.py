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

class Filter():

    def __init__(self,keyWord,hrefList,directoryNumber):
        self.hrefList = hrefList
          
        self.keyWord = keyWord
  
    def filterByKeyword(self):
        keywordListed = []
        for items in self.hrefList:

            if self.keyWord in items:
                keywordListed.append(items)
        return(keywordListed)

    def filterByDirectory(self):
        directoryList= []
        for items in self.hrefList:
            count=Counter(items)
            y = int(count['/'])
            v = self.directoryNumber +2
            x = y -v
            split = items.rsplit('/',x)[0]
            directoryList.append(split)
        return(directoryList)



 
p = Web_Search('https://beavertools.com/brands/amana.html')
hrefList = p.Web_list()
keyWord = 'amana'
x = Filter(keyWord,hrefList,1)

