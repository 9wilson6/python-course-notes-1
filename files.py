# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:41:14 2017

@author: wilson
"""

#open a file

fo = open('test.txt','w')
#print name of the file
print('Name:', fo.name)
#check if file has been closed
print("is closed? ", fo.closed)
#opening mode of the file
print(" opened for :", fo.mode)

# writing into the file
fo.write('i Love programming in python')
fo.write('and Java')
fo.close()
#open to append
fo = open('test.txt','a')
fo.write(' and JavaScript to')
#Open for Reading
fo= open('test.txt','r+')
text=fo.read()
print(text)
fo= open('test.txt','r+')
#read a limited number of text
text2=fo.read(10)
print(text2)
fo.close()

fo=open('test2.txt', 'w+')
fo.write('this is my new file')
fo.close()