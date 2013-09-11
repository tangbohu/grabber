#!/usr/bin/python
# -*- coding: utf-8 -*- 
from conf import *
from user import People
from sendMail import send_mail
import multiprocessing
import threading
import threadpool
from multiprocessing import cpu_count
import web
import time
import signal
import os

class LearingMachine():#threading.Thread):
    UserDict=[]
    def __init__(self):
        self.UserDict=[]
        self.WebDict=[]
        self.interestAll=[]
        self.initPeople()
        self.initWeb()
        self.exit=False
        self.pool=threadpool.ThreadPool(len(self.WebDict))
     
     
    def initPeople(self):
       for item in userdict:
           tempmail=item[0]
           tempinterest=item[1]
           user=People(tempmail,tempinterest)
           interestMap={}
           for intere in tempinterest:
               interestMap[intere]=1
           for value in interestMap:
               self.interestAll.append(value)

           self.UserDict.append(user)
           LearingMachine.UserDict=self.UserDict[:]

    def initWeb(self):
       for item in webdict:
           obj=__import__(item,fromlist=[item])
           func=getattr(obj,item)
           webitem=func(self.interestAll) 
           self.WebDict.append(webitem)
        
    
    def callable_func(self,obj):
        print 'a thread with function runs'
        obj.run()
        return obj

    def callback(self,request,result):
         print 'requestID is',request.requestID,': fetch information is done ,I will classify these message'
         if  result:
                 for user in self.UserDict:
                     userMessage=''
                     found=False
                     for infomation in result.infoVar:
                          userMessage+="tags: "
                          
                          for intere in user.interest:       
                                                 
                             if infomation.tags.has_key(intere):
                                 found=True                               
                                 userMessage+=intere.decode('utf-8')+' '
                          userMessage+="\n"
                          userMessage+=infomation.brief+'\n'+infomation.link+'\n\n'   
                          userMessage+='                         collect by 伯虎大通投行 at '
                          userMessage+= str(time.strftime('%Y-%m-%d %H:%M:%S',result.updateTime)).decode('utf-8')                            
                                       
	             if found:
		             if send_mail(user.mail.decode('utf-8'),str("伯虎大通投行:"+result.fromweb).decode('utf-8'),userMessage):
			         print 'send to ',user.mail ,'done'
			     else :
			         print 'send email error'
                     else:
                          print 'not found userful infomation'
       
  
    def fun(self):
        try:
		print self.UserDict
		requests=threadpool.makeRequests(self.callable_func,self.WebDict,self.callback)
		[self.pool.putRequest(req) for req in requests] 
		self.pool.wait()
        except  KeyboardInterrupt:
            print "!! Ctrl + C entered !!"
            self.exit=True
   

    def run(self):
      try:
         while  not  self.exit:
            before_fun=time.mktime(time.localtime())
            self.fun()
            print "(active worker threads: %i)" % (threading.activeCount()-1, )
            last=time.mktime(time.localtime())-before_fun
            print '总计耗时 ',last,'秒'
            if last>120:
               pass
            else:
               print '一直运行好累，让我睡一会'
               time.sleep(120-last)
      except  KeyboardInterrupt:
            print "!! Ctrl + C entered !!"
            self.exit=True
            #self.stop()


if __name__=='__main__':
   print 'my pid is,',os.getpid()
   print '时区为',time.localtime()
   a=LearingMachine()
   a.run()

