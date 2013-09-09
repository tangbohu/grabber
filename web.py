#!/usr/bin/python
# -*- coding: utf-8 -*- 
import time
import datetime
import sys
import info
import threading
import user
import sendMail
import readWeb

class Web():
   def __init__(self,searchdic=[]):
   #   threading.Thread.__init__(self)
      self.infoVar=[]
      self.searchdict=searchdic
      self.fromweb=""
      self.updateTime=time.localtime()
      t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
      truetime=t[0:11]
      truetime+='00:00:00'
      self.updateTime= time.strptime(truetime, '%Y-%m-%d %H:%M:%S')
   def setSearchDict(self,dic):
       self.searchdict=dic
   def addInfo(self,info):
       self.infoVar.append(info)
   def clearInfo(self):
        self.infoVar[:]=[]
   def collectInfo(self):
       pass
  
   def run(self):
       self.collectInfo()     
#not use
   @staticmethod
   def static_run(obj):
       print 'start run'
       obj.collectInfo()
       print 'run over'
##not use
   @staticmethod
   def callback(web,UserDict):
       if web.infoVar:
                 for user in self.UserDict:
                     userMessage=''
                     found=False
                     for infomation in web.infoVar:
                          userMessage+="tags: "
                          
                          for intere in user.interest:       
                                                 
                             if infomation.tags.has_key(intere):
                                 found=True                               
                                 userMessage+=intere.decode('utf-8')+' '
                          userMessage+="\n"
                          userMessage+=infomation.brief+'\n'+infomation.link+'\n\n'                                 
                                       
	             if found:
		             if send_mail(user.mail.decode('utf-8'),str("伯虎大通投行").decode('utf-8'),userMessage):
			         print 'send to ',user.mail ,'done'
			     else :
			         print 'send email error'
   

