NGRAM
------------

Discrpition
--------------
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



Dependencies
--------------
python-2.7

Usage
-------
   write_short_story.py <book_file_name>

