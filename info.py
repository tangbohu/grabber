#!/usr/bin/python
# -*- coding: utf-8 -*- 
import time
import datetime
import sys
class Info:
   def __init__(self):
      self.link=''
      self.tags={}
      self.brief=''
   def addLink(self,link,brief):
      self.link=link
      self.brief=brief
   def addTag(self,tag):
       self.tags[tag]=1


