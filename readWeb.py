#!/usr/bin/python
# -*- coding: utf-8 -*- 
from BeautifulSoup import BeautifulSoup
import urllib2
import sys
import chardet

def readWeb(url):
       html=urllib2.urlopen(url).read()
       try:
          code=chardet.detect(html)['encoding']
       except:
          code='gb2312'
          print 'could not get decode from web'
       try:
           return BeautifulSoup(html.decode(code,'ignore').encode('utf-8'))
       except:
           print 'exception accur when trying to get soup'
           return BeautifulSoup("")

