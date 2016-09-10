"""
Author : Raghav Bhatnagar
Email : raghavbhatnagar96@gmail.com
Subject : getting data from amazon.
Description:
Getting data from amazon on the basis of query search by the user.
"""

import requests
from bs4 import BeautifulSoup
import multiprocessing
from threading import Thread
finalDict = {}

def AmazonScrape(url):
    s = requests.session()
    headers= {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454.101 Chrome/45.0.2454.101 Safari/537.36'}
    page = s.get(url,headers=headers)
    data = page.text
    soup = BeautifulSoup(data)
    allItems = soup.findAll('div', {'class': 's-item-container'})
    for item in allItems:
        title = item.find('h2').contents[0]
        price = item.find('span', {'class': 'a-size-base a-color-price s-price a-text-bold'})
        if price==None:
            price = item.find('a', {'class': 'a-size-small a-link-normal a-text-normal'}).findAll('span', {'class': 'a-color-price'})[1].contents[-1].encode('utf-8')
        else:
            price = price.contents[1].encode('utf-8')
        title = title.encode('utf-8')
        #print title
        finalDict[title]=('amazon', price)

#searchFor = raw_input("what do you want to search for?  ")
def AmazonGet(search_param):
    url = 'http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='+search_param
    urlArray = []
    for i in range(1,4):
        urlArray.append(url+'&page='+str(i))
    threadlist=[]
    t1 = Thread(target=AmazonScrape ,args=(urlArray[0],))
    t1.start()
    threadlist.append(t1)
    t2 = Thread(target=AmazonScrape ,args=(urlArray[1],))
    t2.start()
    threadlist.append(t2)
    t3 = Thread(target=AmazonScrape ,args=(urlArray[2],))
    t3.start()
    threadlist.append(t3)   
    # print finalDict
    t1.join()
    t2.join()
    t3.join()
    return finalDict


#AmazonGet('iphone') To use, use AmazonGet