#-------------------------------------------------------------------------------
# Name:        filter
# Purpose:
#
# Author:      root
#
# Created:     20/06/2011
# Copyright:   (c) root 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import shlex, subprocess

def main():
  a=p = subprocess.call ('num_generator.py',shell=True)
  print a

if __name__ == '__main__':
    main()
