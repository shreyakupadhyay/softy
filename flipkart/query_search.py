"""
Author : Shreyak Upadhyay
Email : shreyakupadhyay07@gmail.com
Subject : getting data from flipkart .
Description:
Getting data from flipkart on the basis of query search by the user.
"""
import urllib
import requests
from bs4 import BeautifulSoup
import re

def getPage(query):
	url = "http://www.flipkart.com/lc/pr/pv1/spotList1/spot1/productList?sid=search.flipkart.com&start=1&q="+query
	html = requests.get(url)
	#print html
	htmltext = html.text
	return htmltext


def getproduct1(htmltext):
        counter = 1
        try:
            regex_not_f = 'No matching products available.'
            if(regex_not_f in htmltext):
                print "There is no such product pn flipkart"
            else:
                soup = BeautifulSoup(htmltext,'lxml')
                results = soup.findAll('div',attrs={'class':'pu-details lastUnit'})
                j = 0
                for div in results:
                    for data in div.findAll('a',attrs={'class':'fk-display-block'}):
                        value = data.get('title',data.get('href'))
                        if(value is None):
                            continue
                        else:
                            print data['href'] , 'number' , j
                            #print data['title']
                        j=j+1
                    dictionary = {'pu-old':'','pu-off-per else':'','fk-font-17 fk-bold 11':'','fk-font-17 fk-bold':'','pu-emi fk-font-12':''}
                    for data1 in div.findAll('span',attrs={'class':'pu-old'}):
                        if(data1.string!=None):
                            dictionary['pu-old'] = data1.strings
                        print data1.string
                    for data2 in div.findAll('span',attrs={'class':'pu-off-per else'}):
                        if(data2.string!=None):
                            dictionary['pu-off-per else'] = data2.string
                        print data2.string
                    for data3 in div.findAll('span',attrs={'class':'fk-font-17 fk-bold 11'}):
                        if(data3.string!=None):
                            dictionary['fk-font-17 fk-bold 11'] = data3.string
                        print data3.string
                    for data4 in div.findAll('span',attrs={'class':'fk-font-17 fk-bold'}):
                        if(data3.string!=None):
                            dictionary['fk-font-17 fk-bold'] = data4.string
                        print data4.string
                    for data5 in div.findAll('div',attrs={'class':'pu-emi fk-font-12'}):
                        if(data5.string!=None):
                            dictionary['pu-emi fk-font-12'] = data5.string
                        print data5.string
                counter = counter + j
                print counter

        except requests.exceptions.ConnectionError:
            print "Problem in connection with the flipkart server"
getproduct1(getPage("iphone"))