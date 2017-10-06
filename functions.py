# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 19:41:15 2017

@author: wilson
"""
'''FUNCTIONS'''
'''CREAT A FUNCTION'''
def sayHello(name='gatheru'):
    'print hello name'
    print('hello ', name)
sayHello()

'''RETURN A VALUE'''
def getSum(num1, num2):
    total=num1 + num2
    return total
numsum=getSum(30,100)
print(numsum)
'''MUTABLE AND IMMUTABLE VARIABLES'''
def addOneToNum(num):
    num = num +1
    print('Value inside function: ', num)
    return
num=5
addOneToNum(num)

print('Value outside function: ', num)

'''
Value inside function:  6
Value outside function:  5
'''

def addOneToList(myList):
    myList.append(4)
    print('My list inside ',myList)
    return
myList=[1,2,3]
addOneToList(myList)
print('My list outside the function', myList)

'''
My list inside  [1, 2, 3, 4]
My list outside the function [1, 2, 3, 4]
'''






















