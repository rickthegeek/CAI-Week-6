#Project: CIS 177 WEEK 6 PROJECT
#Project Location: projects\cis177\CAI
#File: funcs.py
#Uses: random (standard library)
#Purpose: This file contains the functions specified in
#         the CIS177 week 6 assignment.
#Revision: 1.0 / 27 FEB 2017
#Created: 27 FEB 2017
#Author: Rick Miller <rick@rickthegeek.com>

import random

def getOp():
    # This function will return two random numbers, using the
    # randint() function. No paramaters are needed when calling
    # this function. The numbers returned will be within
    # the range 0-100
    random.seed() # Initialize the random number generator
    op1 = random.randint(0, 100) # generate a random number from 0 thru 100 inclusive
    op2 = random.randint(0, 100) # again for second number
    return(op1, op2)

def getOperator():
    # This function will return a random selection of a character
    # either '+', '-', or '*'. This is done by choosing a random nunber
    # between 1 and 3, 1 will choose +, 2 will choose -, and 3 will be *
    random.seed() # initialize the random number generator
    operator = random.randint(1,3) # pick a random number...
    if operator == 1: # ...then return the character based on the number
        return '+'
    elif operator == 2:
        return '-'
    else:
        return '*'

def doIt(operand1, operand2, operate='+'):
    # This function will perform the chosen operation on the two operands
    # which are passed as parameters to this function. If no operation is
    # indicated, the default operation will be to add.
    if operate == '-':
        return operand1 - operand2
    elif operate == '*':
        return operand1 * operand2
    else: # default is to add, if no operate paramater is given
        return operand1 + operand2

