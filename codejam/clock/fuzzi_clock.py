#-------------------------------------------------------------------------------
# Name:        clock
# Purpose:
#
# Author:      root
#
# Created:     14/06/2011
# Copyright:   (c) root 2011
# Licence:     <your licence>
# Dependencies:
#     python-2.7
#
# Usage:
#    fuzzi_clock.py
#
#    Optionaly you can give a time of your own(in railway time).
#    fuzzi_clock.py <hh:mm:ss>
#-------------------------------------------------------------------------------

#!/usr/bin/env python

"""
    The program prints time with an accuracy of +/-3 minutes in the best verbal
    representation it can (I hope its fuzzy enough).

    The program allows you to print this output in two ways
      1. if you run the program without any command line arguments it takes system
          time and gives an output
      2. if you run the program with a time separated by ':' it uses this as its input

    The program uses two dictionaries to find words for the given time.
    The time of day is decided based on the given hour.
    All this is concatenated into a single string and printed to the consol.


"""

import sys
import time

def main():
  #check if the usage is correct if initialize,else exi with a message.---------
  if len(sys.argv)==2:

    tempstr=sys.argv[1].split(':')
    hour=int(tempstr[0])
    minit=int(tempstr[1])
    sec=int(tempstr[2])
  elif len(sys.argv)==1:
    cur_tm = time.localtime()
    hour=cur_tm.tm_hour
    minit=cur_tm.tm_min
    sec=cur_tm.tm_sec
  else:
    print "Usage: \n\tfuzzi_clock.py\n\n\tOptionaly you can give a time of your own."
    print "\tfuzzi_clock.py <hh:mm:ss>"
    sys.exit(1)
  #-----------------------------------------------------------------------------

  #Dictionaries for the program-------------------------------------------------
  num2word={
  0:'',
  1:'One',
  2:'Two',
  3:'Three',
  4:'Four',
  5:'Five',
  6:'Six',
  7:'Seven',
  8:'Eight',
  9:'Nine',
  10:'Ten',
  11:'Eleven',
  12:'Twelve',
  15:'Quarter',
  20:'Twenty',
  25:'Twenty-Five',
  30:'Half'
  }

  nearness={
  0:'now ',
  1:'arround ',
  2:'about ',
  3:'almost ',
  4:'nearly '
  }
  #-----------------------------------------------------------------------------

#print the time under consideration---------------------------------------------
  print hour,':',minit,':',sec

  #find the time of day---------------------------------------------------------
  if hour>=11 and hour <=15:
    time_of_day=' at noon.'
  elif hour>15 and hour<20:
    time_of_day=' in the evening.'
  elif hour>=20 or hour<2:
    time_of_day=' at night.'
  elif hour>=2 and hour <6:
    time_of_day=' early morning.'
  else:
    time_of_day=' in the morning.'
  #time of day found out--------------------------------------------------------

  #change to twelve hour clock--------------------------------------------------
  if hour>12:
    hour-=12
  #-----------------------------------------------------------------------------

  #finding nearness ,connection string and the hour to talk about---------------
  temp=minit%5
  connect_str=' past '

  if temp>2 and minit<=30:
    x=minit+(5-temp)
  elif temp>2 and minit>30:
    x=60-minit-(5-temp)
    hour=hour+1
    connect_str=' to '
  elif temp<3 and minit>30:
    x=60-minit+temp
    hour=hour+1
    connect_str=' to '
  else:
    x=minit-temp

  if minit<3 or minit>57:
    connect_str=''
  #-----------------------------------------------------------------------------

  #finaly finding the string to represent the time------------------------------
  ct_str='Its '
  ct_str+=nearness[temp]+num2word[x]+connect_str+num2word[hour]+time_of_day
  print ct_str


if __name__ == '__main__':
    main()
