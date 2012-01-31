#-------------------------------------------------------------------------------
# Name:        mirror
# Purpose:
#
# Author:      root
#
# Created:     20/06/2011
# Copyright:   (c) root 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import time
import sys
import urlparse
from urllib2 import urlopen
from urllib import urlretrieve
import scipy as sp
from scipy.misc import imread
from scipy.signal.signaltools import correlate2d as c2d

def get(i):
   # get JPG image as Scipy array, RGB (3 layer)
  data = imread(i)
  # convert to grey-scale using W3C luminance calc
  data = sp.inner(data, [299, 587, 114]) / 1000.0
  # normalize per http://en.wikipedia.org/wiki/Cross-correlation
  return (data - data.mean()) / data.std()


def main():
  if len(sys.argv)!=3:
    print 'Usage: mirror.py <url1> <url2>'
    sys.exit(-1)
  outfile1=sys.argv[1].split('/')[-1]
  urlretrieve(sys.argv[1],outfile1 )
  outfile2=sys.argv[2].split('/')[-1]
  urlretrieve(sys.argv[2],outfile2 )
  print 'start'
  im1 = get(outfile1)
  print 'got img 1'
  im2=get(outfile2)
  ti=time.time()
  print  im1.shape, im2.shape
  c11 = c2d(im1, im1, mode='same')
  print c11.max(),time.time()-ti
  ti=time.time()
  c12 = c2d(im1, im2, mode='same')
  print  c12.max(),time.time()-ti
  print 'Similarity :',((c12.max()/c11.max())*100)

if __name__ == '__main__':
  main()
