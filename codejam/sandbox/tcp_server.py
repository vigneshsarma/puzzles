#-------------------------------------------------------------------------------
# Name:        sandbox
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
This is the tcp server.
"""

from socket import *
import os
import time

class MyServer:
  """
  A simple TCP server with options [list,pwd ,rm,touch,time].
  """
  def __init__(self):
    """Server is initialized"""
    self.HOST = ''    #we are the host
    self.PORT = 29876    #arbitrary port not currently in use
    self.ADDR = (self.HOST,self.PORT)    #we need a tuple for the address
    self.BUFSIZE = 4096    #reasonably sized buffer for data
    self.serv = socket( AF_INET,SOCK_STREAM)

  def start(self):
    """
    Start the server and get a connection.Do a hand shake.
    """
    ##bind our socket to the address
    self.serv.bind((self.ADDR))    #the double parens are to create a tuple with one element
    self.serv.listen(5)    #5 is the maximum number of queued connections we'll allow

    print 'listening...'

    self.conn,addr = self.serv.accept() #accept the connection
    print '...connected!'
    self.conn.send('READY')
    data = self.conn.recv(self.BUFSIZE)
    print data
    self._running()

  def _running(self):
    """
    The server is running.When a new data comes in if it is 'close' it shutsdown
    else it passes the value as argument to handle_option().
    """
    data = self.conn.recv(self.BUFSIZE)
    print data

    while(data!='close'):
      response=self.handle_option(data)
      self.conn.send(response)
      data = self.conn.recv(self.BUFSIZE)

  def handle_option(self,data):
    """
    The function takes the data and performes the action and returns some result.
    """
    response=''
    if data=='list':
      for files in os.listdir('.'):
        response+=files+' '

    elif data=='pwd':
      response+=os.path.abspath('.')

    elif data[:3]=='cat':
      try:
        f=open(data[4:])
        response+=data[4:]+':\n'
        for lines in f:
          response+=lines+' '
      except IOError:
        response+='File Not found'

    elif data[:2]=='rm':
      try:
        os.remove(data[3:])
        response+='File deleated '+data[3:]
      except WindowsError:
        response+='File not found '+data[3:]

    elif data[:5]=='touch':
      d=data.split()
      f=open(d[1],'w')
      if d[2][0]=='$':#the touch command alone has the ability to execute its last
        #parameter if it starts with '$' symbol
        f.write(self.handle_option(d[2][1:]))
      else:
        f.write(d[2])
      f.close()
      response+='FILE CREATED : '+d[1]

    elif data=='time':
      response=time.ctime()

    elif data=='help':
      response+='[list,pwd ,rm,touch,time]'

    else:
      response+='ERROR [help close]'

    return response

  def close(self):
    """
    called at the end of a connection.
    """
    self.conn.close()


def main():
  """
  Main that starts the server.
  """
  serv=MyServer()
  serv.start()
  serv.close()


if __name__ == '__main__':
    main()
