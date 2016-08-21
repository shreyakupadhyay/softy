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

def AmazonScrape(url):
    s = requests.session()
    headers= {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454.101 Chrome/45.0.2454.101 Safari/537.36'}
    page = s.get(url,headers=headers)
    data = page.text
    soup = BeautifulSoup(data)
    allItems = soup.findAll('div', {'class': 's-item-container'})
    for item in allItems:
        print item.find('h2').contents[0]
        price = item.find('span', {'class': 'a-size-base a-color-price s-price a-text-bold'})
        if price==None:
            print 'offers from: Rs.'+item.find('a', {'class': 'a-size-small a-link-normal a-text-normal'}).findAll('span', {'class': 'a-color-price'})[1].contents[-1].encode('ascii')
        else:
            print 'Rs. ' + price.contents[1].encode('ascii')
        print '...........'
    print 'END OF FUNC '+ url[-1]+' ...........................................................'

searchFor = raw_input("what do you want to search for?  ")
params = searchFor.split(" ")
url = 'http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='+searchFor
urlArray = []
for i in range(1,4):
     urlArray.append(url+'&page='+str(i))
#print urlArray
pool = multiprocessing.Pool(processes=3) # how much parallelism?
pool.map(AmazonScrape, urlArray)











# p.start()
# p.join()
# q = multiprocessing.Process(target=AmazonScrape, args=(url, 2))
# q.start()
# q.join()
# for eachparam in params:
#     url = url + eachparam + "+"
#url2= 'http://www.google.com'
#print url
# s = requests.session()
# headers= {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454.101 Chrome/45.0.2454.101 Safari/537.36'}
# page = s.get(url,headers=headers)
# data = page.text
# soup = BeautifulSoup(data)
# #print 'souping done'
# allItems = soup.findAll('div', {'class': 's-item-container'})
# for item in allItems:
#     print item.find('h2').contents[0]
#     price = item.find('span', {'class': 'a-size-base a-color-price s-price a-text-bold'})
#     if price==None:
#         print 'offers from: Rs.'+item.find('a', {'class': 'a-size-small a-link-normal a-text-normal'}).findAll('span', {'class': 'a-color-price'})[1].contents[-1].encode('ascii')
#     else:
#         print 'Rs. ' + price.contents[1].encode('ascii')
#     print '...........'
# url2 = url+'&page=2'
# page = s.get(url2,headers=headers)
# data = page.text
# soup = BeautifulSoup(data)
# #print 'souping done'
# allItems = soup.findAll('div', {'class': 's-item-container'})
# for item in allItems:
#     print item.find('h2').contents[0]
#     price = item.find('span', {'class': 'a-size-base a-color-price s-price a-text-bold'})
#     if price==None:
#         print 'offers from: Rs.'+item.find('a', {'class': 'a-size-small a-link-normal a-text-normal'}).findAll('span', {'class': 'a-color-price'})[1].contents[-1].encode('ascii')
#     else:
#         print 'Rs. ' + price.contents[1].encode('ascii')
#     print '...........'

#for link in soup.find_all('a'):
#   print(link.get('href'))
# mydivs = soup.findAll("a", { "class" : "a-link-normal s-access-detail-page  a-text-normal" })
# myprice = soup.findAll("span", { "class" : "a-size-base a-color-price s-price a-text-bold" })
# #print mydivs[0]['title']
# print myprice[0]
# print soup.title
#print mydivs
#raw_input()
#print soup
