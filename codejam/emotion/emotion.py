#-------------------------------------------------------------------------------
# Name:        emotion
# Purpose:
#
# Author:      root
#
# Created:     19/06/2011
# Copyright:   (c) root 2011
# Licence:     <your licence>
# Dependencies:
#     python-2.7
#     twython
#     simplejson
#     oauth2
#-
#
# Usage:
#    emotion.py
#
#    By default it searches for the 100sec but after 10 sec, it asks whether
#    you want to continue.If you don't type something there.
#-------------------------------------------------------------------------------
#!/usr/bin/env python
"""
The program uses the twython library to get search results on twitter.
From the result the Data for the last 10 sec is extracted.
Askes whether you want to continue.If you don't type some thing.Else it sleeps for
10 sec and continues.By defaultit stops after 100sec.
Now it generates a graph using Tkinter, Showing the result.

"""
from twython import Twython
from datetime import datetime
import re
import time
import Tkinter as tk
import threading

conti='yes'

class ContinueThread ( threading.Thread ):
  """
  The class maintains a thread that checks whether user wants to stop.
  """
  def __init__(self):
    super(ContinueThread, self).__init__()

  def run ( self ):
    global conti
    conti=raw_input()

def graph_points(seq, width=375, height=325):
  """
  This function is used to draw graph.
  """
  root = tk.Tk()
  c = tk.Canvas(root, width=width, height=height, bg='white')
  c.pack()
  y_stretch = 2
  y_gap = 20
  x_stretch = 10
  x_width = 20
  x_gap = 20
  for x, y in enumerate(data):
    x0 = x * x_stretch + x * x_width + x_gap
    y0 = height - (y * y_stretch + y_gap)
    x1 = x * x_stretch + x * x_width + x_width + x_gap
    y1 = height - y_gap
    c.create_rectangle(x0, y0, x1, y1, fill="red")
    c.create_text(x0+2, y0, anchor=tk.SW, text=str(y))
    c.create_text(x0+2, 2, anchor=tk.SW, text=str(x))
  root.mainloop()

def sort_res(res_tim):
  """
  Searches the given list for time and returns the number of posts,and the last time it considerded.
  """
  i=0
  length=0
  for each in res_tim:
    mat=re.search(r'(\d\d:\d\d:\d\d)',each)
    if mat and i!=10:
      if i==0:
        hr=mat.group(1)
        i+=1
      elif i==10:
        break
      elif not mat.group(1)==hr:
        i+=1
        hr=mat.group(1)
      length+=1
    else:
      break
  return length,hr

data=[]

def main():
  twitter = Twython()
  count=0

  while(count<10 and conti=='yes'):
    dtnow=datetime.utcnow()
    tm_now=time.time()
    dt_str=str(dtnow.day)+' '+str(dtnow.month)+' '+str(dtnow.year)+' '+str(dtnow.hour)+':'+str(dtnow.minute)+':'+str(dtnow.second) +' +'+str(dtnow.microsecond)

    results = twitter.searchTwitter(q="i love you",since_id=dt_str,rpp='100',result_type='recent')

    res_tim=[]
    if results:
      print '\ngot result',len(results[u'results']),dt_str
      for each in results[u'results']:
        res_tim.append(each[u'created_at'])

    data1=sort_res(res_tim)
    print data1
    data.append(data1[0])

    if count==0:
      ContinueThread().start()
    print 'Do you want to continue(there is a time-out of 10sec):',

    time.sleep(10-int(time.time()-tm_now))
    count+=1

  graph_points(data1)


if __name__ == '__main__':
    main()
