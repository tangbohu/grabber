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




class zcwyb(Web):
    def __init__(self,dic):
         Web.__init__(self,dic)
         self.url='http://stock.cfi.cn/BCA0A4127A4346A4440.html'
         self.soup=None
         self.fromweb="中财网研报"
         print '中财网研报启动成功'
             

    def getChildSoup(self,link):
        childSoup=self.readWeb(link)
        return childSoup  
  
    def searchTag(self,strinfo):
          result=[]
          for key in self.searchdict:
             if(strinfo.find(key)!=-1):
                print 'find ',key
	        result.append(key)
	  return  result



    def linkAnalysis(self,link):
        temp=link.findAll("a")
        dat=link.findAll("span")
        i=0
        for da in dat:
            strtemp=da.string
            if  strtemp.find(':')==-1:
                 return
            else:
                address='http://stock.cfi.cn/'+temp[i]["href"]
                brief=temp[i].string
                t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                truetime=t[0:11]+strtemp+':59'
                now= time.strptime(truetime, '%Y-%m-%d %H:%M:%S')
                if time.mktime(now)<time.mktime(self.updateTime):
                   return
                else :
                    print 'link address is : ',address 
		childSoup=self.getChildSoup(address)   
                try:   
		   newsContent=childSoup.find(attrs={"id":"tdcontent"})
                except:
                   newsContent=None

		stringTemp=""
		if not newsContent:
		    return 
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
		print '------------------------- one link analysis end ','------------------'
                i+=1

        

    def collectInfo(self):
        self.clearInfo()
        self.soup=readWeb(self.url)
        temptime=time.localtime()
        print '======================从',self.fromweb,'搜集信息了啊======================='
        try:
            linkVector=self.soup.findAll(attrs={"class":"xinwen"})
            self.linkAnalysis(linkVector[0])   
        except:
              print 'error accur when get the list of the information from ',self.fromweb
        self.updateTime=temptime
        print '从',self.fromweb,'读取信息成功'

        

if __name__=='__main__':

    search=['平安银行']
    a=zcwyb(search)
    a.collectInfo()
    
    
