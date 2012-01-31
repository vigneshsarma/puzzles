#-------------------------------------------------------------------------------
# Name:        num_generator
# Purpose:
#
# Author:      root
#
# Created:     20/06/2011
# Copyright:   (c) root 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import random


def main():
  random.seed()
  #while True:
  all=random.getstate()
  for each in all[1]:
    if len(str(each))==10:
      print each
  #if raw_input('>>')=='no':
    break


if __name__ == '__main__':
    main()
