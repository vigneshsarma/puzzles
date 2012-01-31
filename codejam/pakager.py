#-------------------------------------------------------------------------------
# Name:        pakager
# Purpose:
#
# Author:      root
#
# Created:     13/06/2011
# Copyright:   (c) root 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys,re
from zipfile import ZipFile

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

gmail_user = "vignesh.sarma@gmail.com"
gmail_pwd = "fire1flame2flow3"

def mail(to, subject, text, attach):
   msg = MIMEMultipart()

   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach, 'rb').read())
   Encoders.encode_base64(part)
   part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()


def main():
##  f=open( sys.argv[1])

  val=0
  discrpition=[]
  usage=[]
  dependencies=[]
  fullname='vignesh_sarma_k'
  passoutyear='2012'
  contestID='sandbox'
##  for lines in f:
##    print lines,
##    if val==0:
##      mat=re.search(r'Name:\s+(\w+)',lines)
##      if mat:
##        val+=1
##        contestID=mat.group(1)
##    elif val==1:
##      mat=re.search(r'Dependencies:',lines)
##      if mat:
##        val+=1
##    elif val==2:
##      mat=re.search(r'#-',lines)
##      if not mat:
##        dependencies.append(lines[1:])
##      else:
##        val+=1
##    elif val==3:
##      mat=re.search(r'Usage:',lines)
##      if mat:
##        val+=1
##    elif val==4:
##      mat=re.search(r'#----',lines)
##      if not mat:
##        usage.append(lines[1:])
##      else:
##        val+=1
##    elif val==5:
##      mat=re.search(r'"""',lines)
##      if mat:
##        val+=1
##    elif val==6:
##      mat=re.search(r'"""',lines)
##      if not mat:
##        discrpition.append(lines)
##      else:
##        val+=1
##        break
##
##
##  print contestID,dependencies,usage,discrpition
##  f.close()
##
##  readme=open(contestID+'/readme.txt','w')
##  readme.write(contestID.upper()+'\n------------')
##  readme.write('\n\nDiscription\n--------------\n')
##  for line in discrpition:
##    readme.write(line)
##  readme.write('\nDependencies\n--------------\n')
##  for line in dependencies:
##    readme.write(line)
##  readme.write('\nUsage\n-------\n')
##  for line in usage:
##    readme.write(line)
##  readme.close()
  atach=contestID+'/'+fullname+'_'+passoutyear+'_'+contestID+'.zip'
  with ZipFile(atach, 'w') as myzip:
    myzip.write(contestID+'/readme.txt')
    myzip.write(contestID+'/client.py')
    myzip.write(contestID+'/tcp_server.py')
    myzip.write(contestID+'/client.htm')
    myzip.write(contestID+'/tcp_server.htm')

  mail('codejam@mobme.in','Submission for contest '+contestID,'',atach)

if __name__ == '__main__':
    main()
