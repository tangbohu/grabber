#!/usr/bin/python
# -*- coding: utf-8 -*- 
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

SMTP_SERVER='smtp.gmail.com'
SMTP_PORT=587

mailto_list=["981501515@qq.com"]
mail_host="smtp.gmail.com" 
mail_sender='bohu.morgan@gmail.com'
mail_pass="bohumorgan"

def send_mail(to_list,sub,content):
    msg = MIMEText(content,'plain','utf-8')
    msg['Subject'] = sub
    msg['From'] = mail_sender
    msg['To'] = ";".join(to_list)
    try:

        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(mail_sender, mail_pass)
        session.sendmail(mail_sender, to_list, msg.as_string())
        session.quit()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__=='__main__':
    if send_mail(mailto_list,"subject","content"):
        print "send done!"
    else:
        print "error occur!"

