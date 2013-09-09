#!/usr/bin/python
# -*- coding: utf-8 -*- 
"""dong fang cai fu wang"""

from web import Web
from BeautifulSoup import BeautifulSoup

import urllib2
import sys
import chardet
import time
import datetime
from info import Info
from readWeb import readWeb 




class dfcfw(Web):
    def __init__(self,dic):
         Web.__init__(self,dic)
         self.url='http://stock.eastmoney.com/news/cgszb.html'
         self.soup=None
         self.fromweb="东方财富网"
         print '东方财富网初始化成功'
             

    def getChildSoup(self,link):
        childSoup=readWeb(link)
        return childSoup  
  
    def searchTag(self,strinfo):
          result=[]
          for key in self.searchdict:
             if(strinfo.find(key)!=-1):
                print 'find ',key
	        result.append(key)
	     else:
                 pass
	  return  result



    def linkAnalysis(self,link):
        temp=link.find("a")
        address=temp["href"]   
        brief=temp["title"]   
        timenow=link.find("span").string
        timenow+=":59"
        now= time.strptime(timenow, '%Y-%m-%d %H:%M:%S')
    #    print 'news time:',timenow,'and last update time :',self.updateTime
        if time.mktime(now)<time.mktime(self.updateTime):
          
            return 0
       
        print 'link address is : ',address 
        childSoup=self.getChildSoup(address)      
        try:
           newsContent=childSoup.find(attrs={"class":"Body","id":"ContentBody"})
        except:
           newsContent=None

        stringTemp=""
 
        if newsContent==None:
            return 1
        for content in newsContent:
            stringTemp+=str(content)

        tags=self.searchTag(stringTemp)

        if tags:
               newin=Info()
               newin.addLink(address,brief)
               for tag  in tags:
                  newin.addTag(tag)
                  print 'in this news find ',tag
               self.addInfo(newin)
        print '------------------------- one link analysis end -------------------------'
        return 1
        

    def collectInfo(self):
        self.clearInfo()
        self.soup=readWeb(self.url)
        temptime=time.localtime()
        print '======================从东方财富网搜集信息了啊======================='
        print 'last updateTime is ', time.strftime('%Y-%m-%d %H:%M:%S',self.updateTime)
        try:
		linkVector=self.soup.find(attrs={"class":"list"}).findAll(name="li")
		for link in linkVector:
		    if not self.linkAnalysis(link):
			 break
        except:
               print 'error accur when get the list of the information from ',self.fromweb

        self.updateTime=temptime
        print '从',self.fromweb,'读取信息成功'
    

        

if __name__=='__main__':
    search=['平安银行']
    a=dfcfw(search)
    while True:
       a.collectInfo()
    
    
