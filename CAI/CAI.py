#Project: CIS 177 WEEK 6 PROJECT
#Project Location: projects\cis177\CAI
#File: CAI.py
#Uses: funcs.py (Library containing the math functions for choosing problems)
#Purpose: Asks the user ten math questions one at a time,
#         gives the user feedback and keeps track of the score
#Revision: 1.0 / 27 FEB 2017
#Created: 27 FEB 2017
#Author: Rick Miller <rick@rickthegeek.com>

import funcs # import the functions file containing the math functions

numberOfProblems = 10 # change this to ask more or fewer problems
score = 0 # user's score
problemNumber = 1 # initialize this to 1. Humans count from 1 so this will make sense to the user
debug = False # change to true to enable debug mode

def displayProblem(problemNumber):
    # get two random numbers, and return the right answer to the problem
    # the problem number is passed to this function and will be displayed
    # with the problem.
    op1, op2 = funcs.getOp() # get the operands...
    operand = funcs.getOperator() # ...and the operator
    print('Problem',problemNumber, ':', op1, operand, op2, '=') #display the problem
    return funcs.doIt(op1, op2, operand) # do the math and return the answer

while problemNumber <= numberOfProblems:
    correctAnswer = displayProblem(problemNumber)
    if debug: 
        print('Answer =', correctAnswer) # show correct answer if we are in debug mode
    userAnswer = int(input('What is your answer? ')) # convert to user input to int
    if debug:
        print('UserAnswer=',userAnswer) # show user's answer if in debug mode
    if userAnswer == correctAnswer: # congratulate the user and add a point to the score
        print('Correct!\n')
        score += 1
    else: # tell the user, but no point added
        print('Incorrect\n')
    problemNumber += 1
print('Finished! You got', score, 'correct out of', numberOfProblems)
