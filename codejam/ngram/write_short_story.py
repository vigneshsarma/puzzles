#-------------------------------------------------------------------------------
# Name:        ngram
# Purpose:
#
# Author:      vignesh_sarma_k
#
# Created:     13/06/2011
# Licence:     <your licence>
#
# Dependencies:
#     python-2.7
#
# Usage:
#   write_short_story.py <book_file_name>
#
#-------------------------------------------------------------------------------
#!/usr/bin/env python

"""
    First of the program loops through the given file finding trigrams and storing
    them to a dictionary. Dictionary is of the form with the first word in the trigrams
    is used as the key and the other words are added to a list of size 2.with each
    element in a list of its own. Following figure illustrates this .
          ->[2nd,2nd,...]
    [1st]|->[3rd,3rd,...]

    A word is anything  separated by a space and its self not a space. Thus there
    might be same words in the dictionary one with a capital to start, another with some
    punctuation ,one the real word itself. This is because the words associated with a
    Word starting with a capital letter has different meanings, similarly with punctuation.

    The story itself starts when the program is able to find a word randomly that
    Starts in capitol letter.

    Again the story end when it has printed at least 200 characters and the given word ends
    in a full stop.

    Whenever and wherever possible randomization is done to ensure we get a different
    story each time.

    Elements in the list are deleted once the are used .Else sometimes the program
    keeps cycling through sentences.


"""
import random
import sys

def main():
  if len(sys.argv)!=2 :
    print 'Usage: write_short_story.py <book_file_name>'
    sys.exit(1)

  filename=sys.argv[1]
  try:
    f=open(filename,'r')
  except IOError:
    print 'file not vald'
    sys.exit(1)
  theDict={}
  word1=''
  word2=''
  word3=''


#----------sort all words into a dictionary-------------------------------------
  for lines in f:
    for words in lines.split():
      #swap words
      word3,word2,word1=word2,word1,words
      if word3 and not word3.isspace() and word2 and not word2.isspace():
        if word3 in theDict:
          theDict[word3][0].append(word2)
          theDict[word3][1].append(word1)
        else:
          theDict[word3]=[[word2],[word1]]

#-------------------------------------------------------------------------------

  #To see the dictionary uncomment these lines
##  for stuf in sorted(theDict.items()):
##    print stuf

  #------chose a random word that starts with caps------------------------------
  word1='a'
  while(word1[0].islower()):
    word1=random.choice(theDict.keys())
  #-----------------------------------------------------------------------------


  word2=''
  word3=''

  print '\t\tSTORY'
  print '\t\t-----'
  linelen=0
  #----finaly the story,it can have up to 300 words but atleast 200-------------
  for i in range(0,300):
    print word1,
    linelen+=len(word1)
    if linelen>70:
      print
      linelen=0

    #-----after 200 printing stopsat the first word it encounters that ends in
    #-----fullstop--------------------------------------------------------------
    if i>=200 and word1[-1]=='.':
      break
    i=0
    #making sure that the nixt word is part ofthe triagram----------------------
    if not word3 and not word2:
      index1=random.choice(range(0,len(theDict[word1][0])))
      word2,word3=theDict[word1][0][index1],theDict[word1][1][index1]
      #without deleating the words once usesd the program semes to cycle arround
      #some scentences repeating them again and again.
      del theDict[word1][0][index1]
      del theDict[word1][1][index1]
    else:
      consider=theDict[word1][0]
      index1=[consider.index(word2)]
      #----This to make sure each time we get a different story-----------------
      while i<len(consider):
        if word2 in consider[(index1[-1]+1):]:
          index1.append(consider[(index1[-1]+1):].index(word2)+(index1[-1]+1))
        else:
          break
        i+=1
      index1=random.choice(index1)
      #-------------------------------------------------------------------------
      word3=theDict[word1][1][index1]
      del theDict[word1][0][index1]
      del theDict[word1][1][index1]
    #swap words
    word1,word2=word2,word3



if __name__ == '__main__':
    main()
