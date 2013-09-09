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
    

  
    
    @staticmethod
    def callable_func(obj):
        print 'a thread with function runs'
        obj.run()
        return obj

    @staticmethod
    def callback(request,result):
         print 'requestID is',request.requestID,': fetch information is done ,I will classify these message'
         if  result:
                 for user in LearingMachine.UserDict:
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
                                       
	             if found:
		             if send_mail(user.mail.decode('utf-8'),str("伯虎大通投行:"+result.fromweb).decode('utf-8'),userMessage):
			         print 'send to ',user.mail ,'done'
			     else :
			         print 'send email error'
                     else:
                          print 'not found userful infomation'
       
  
    def fun(self):
        print webdict
        pool=threadpool.ThreadPool(len(webdict))
        requests=threadpool.makeRequests(LearingMachine.callable_func,self.WebDict,LearingMachine.callback)
        [pool.putRequest(req) for req in requests] 
        pool.wait()
   
             

    def run(self):
      try:
         while  not  self.exit:
            before_fun=time.mktime(time.localtime())
            self.fun()
            last=time.mktime(time.localtime())-before_fun
            print '总计耗时 ',last,'秒'
            if last>60:
               pass
            else:
               print '一直运行好累，让我睡一会'
               time.sleep(60-last)
      except  KeyboardInterrupt:
            print "!! Ctrl + C entered !!"
            self.exit=True
            #self.stop()
            

        

    

if __name__=='__main__':
   print 'my pid is,',os.getpid()
   a=LearingMachine()
   a.run()

