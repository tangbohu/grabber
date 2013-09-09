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



class thstzjh(Web):
    def __init__(self,dic):
         Web.__init__(self,dic)
         self.url='http://stock.10jqka.com.cn/tzjh_list/'
         self.soup=None
         self.fromweb="同花顺投资机会"
         print '同花顺投资机会初始化成功'
             

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
        print 'link address is : ',address 
        timenow=link.find(attrs={"class":"date"}).string
    #    print timenow
        y=timenow[0:4]
        m=timenow[5:7]
        d=timenow[8:10]
        second=timenow[12:20]
        timenow=y+'-'+m+'-'+d+' '+second
        now= time.strptime(timenow, '%Y-%m-%d %H:%M:%S')

        if time.mktime(now)<time.mktime(self.updateTime):

            return 0
  
          
        childSoup=self.getChildSoup(address)      
        try:
           newsContent=childSoup.find(attrs={"class":"art_main"})
        except:
           newsContent=None

        stringTemp=""
        if not newsContent:
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
        print '------------------------- one link analysis end ---------------------'
        return 1
        

    def collectInfo(self):
        self.clearInfo()
        self.soup=readWeb(self.url)
        temptime=time.localtime()
        print '======================从',self.fromweb,'搜集信息了啊======================='
        linkVector=self.soup.findAll(attrs={"class":"list_item"})
        try:
		for link in linkVector:
		    if not self.linkAnalysis(link):
		         break
        except:
              print 'error accur when get the list of the information from ',self.fromweb

        self.updateTime=temptime
        print '从',self.fromweb,'读取信息成功'
    

        

if __name__=='__main__':
    search=['哈尔滨工业大学']
    a=thstzjh(search)
    a.collectInfo()
    
    
