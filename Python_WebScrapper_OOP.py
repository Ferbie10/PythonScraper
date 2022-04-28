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

class Filter():

    def __init__(self,hrefList):
        self.hrefList = hrefList
          
        
    classmethod
    def filterByKeyword(cls,keyWord):
        keywordListed = []
        cls.keyWord = keyWord
        for items in cls.hrefList:

            if cls.keyWord in items:
                keywordListed.append(items)
        return(keywordListed)
    classmethod

    def filterByDirectory(cls,folderNumber):
        directoryList= []
        cls.folderNumber = folderNumber
        for items in cls.hrefList:
            count=Counter(items)
            y = int(count['/'])
            v = cls.directoryNumber +2
            x = y -v
            split = items.rsplit('/',x)[0]
            directoryList.append(split)
        return(directoryList)



 




def main():
    x =0
    while True:
        userAnswer = input('Do you wish run again? (Y)es or (N)o: ').upper()
        os.system('cls')
        while userAnswer == 'Y':
            userURL = input('Please, enter a URL:  ')
            try:
                url = Web_Search(userURL)
                hrefList=url.webSeach()
                doFilter = int(input('Do you wish to filter the results by [1]keyword, or [2]folder number:  '))
                if doFilter == 1:
                    keyWord = input('Enter the keyword you would like to search by:  ')
                    filtered = Filter(hrefList)
                    keywordFiltered=filtered.filterByKeyword(keyWord)
                    break
                elif doFilter == 2:
                    folderNumber = int(input('What folder number would you like to filter by:  '))
                    filtered = Filter(hrefList)
                    folderNumberFilter = filtered.filterByDirectory(folderNumber)
                    break
                else:
                    print("Invaild selection, Please enter 1 for keyword or 2 for folder number:")
            except:
                print("Invaild URL Please Try again")
        
                
    

main()