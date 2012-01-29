#Gymnast Tower Routine Puzzle
###Puzzle Description
A gymnast center is designing a tower routine consisting of people standing on top of other’s shoulders. For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her.
Given the heights and weights of each person in the event, write a program that computes the largest possible number of people in such a tower routine.
The program accepts a single argument on the command line. This argument is a file name, which contains the information you need (the heights and weights of each person). The program must write to the standard output the largest possible number of people in the tower, followed by a single newline (‘\n’).
###Input Specifications

The input file consists of a single line.
The line is made of pairs of heights and weights. Each pair is in the format (ht, wt), with ht and wt both positive integers.
Each pair is separated by a whitespace. The line might or might not be terminated by a new line ‘\n’.
There are no gymnasts having the same height or same weight.
Here is an example of a valid input: 

`(15, 176) (65, 97) (72, 43) (102, 6) (191, 189) (90, 163) (44, 168) (39, 47) (123, 37)`
###Output Specifications

Your program should output on the standard output the largest possible number of people in the tower, followed by a single newline (‘\n’).
Here is an example of a valid output: 

`4`

###Test Cases
Your program will be executed as follows (example is for a Ruby submission):

`./gymnast.rb a.in`
