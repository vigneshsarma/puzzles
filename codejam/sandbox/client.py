#-------------------------------------------------------------------------------
# Name:        client
# Purpose:
#
# Author:      root
#
# Created:     19/06/2011
# Copyright:   (c) root 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

"""
Client program .It has two threads.
  1. the main thread itself,through which you can request for verious services.
  2. A secondary thread ,which becomes active every 1min to create a file with a
      random name and server time as content.
"""
from socket import *
import time
import threading
import sys
import random,string

some_one=False
main_alive=True

class ClientThread ( threading.Thread ):
  """
  Active once every 1 min.create a file with a random file name.
  """

  def __init__(self,con,BUFSIZE):
    super(ClientThread, self).__init__()
    self.cli = con
    self.BUFSIZE=BUFSIZE
    self._stop = threading.Event()

  def run ( self ):
    """Body of the thread.Dies when the main thread is no longer alive"""
    global some_one,main_alive
    while main_alive:
      if not some_one:
        some_one=True
        name=''.join(random.choice(string.ascii_uppercase +
        string.digits) for x in range(6))#generate a random file name.
        try:
          self.cli.send('touch '+name+'.TXT $time')
          data = self.cli.recv(self.BUFSIZE)
          print '\n',data,'\n >?'
        except error:
          print 'connection faild'
          sys.exit(1)
        some_one=False
        i=0
        while main_alive and i<59:
          time.sleep(1)
          i+=1

  def stop (self):
        self._stop.set()

def main():
  """Client program ."""
  HOST = 'localhost'
  PORT = 29876    #our port from before
  ADDR = (HOST,PORT)
  BUFSIZE = 4096

  global some_one,main_alive  #global variables

  cli = socket( AF_INET,SOCK_STREAM)#initialize a scocket

  try:#try to get a connection
    cli.connect((ADDR))
  except error:
    print 'Server refuced connection ,try later'
    sys.exit(1)

  data = cli.recv(BUFSIZE)
  cli.send(data)
  print data

  back_thr=ClientThread(cli,BUFSIZE)
  back_thr.start()

  data=raw_input(' >? ')
  while(data!='close' and not some_one ):
    some_one=True
    cli.send(data)
    data = cli.recv(BUFSIZE)
    some_one=False
    print data
    data=raw_input(' >? ')

  cli.send('close')
  cli.close()
  main_alive=False
  back_thr.stop()
  sys.exit(0)

if __name__ == '__main__':
    main()
