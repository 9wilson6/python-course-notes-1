# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 21:30:40 2017

@author: wilson
"""

'''String functions'''
mystring="hello world"
mystring1="helloWorld"
#capitalize
print(mystring.capitalize())
'''Hello world'''
#swapcase
print(mystring.swapcase())
'''HELLO WORLD'''
'''get Length'''
print(len(mystring))
'''11'''
'''replace'''
print(mystring.replace('hello','holla'))
'''holla world'''


'''count numberb of times an element occurs'''

sub='l'
print(mystring.count(sub))

'''3'''

'''Starts with $ ends with'''

print(mystring.startswith('h'))

''' True'''

print(mystring.startswith('hello'))

''' True'''

print(mystring.startswith('world'))

''' False'''

'''Ends With'''
print(mystring.endswith('world'))

"True"



#split String int a list
myLst=mystring.split(' ')
print(myLst)
'''['hello', 'world']'''


myLst=mystring.split()
print(myLst)
'''['hello', 'world']'''

'''find position of a string'''
print(mystring.find('world'))

""" 6 """
print(mystring.find('h'))

'''0'''


"""Is alpha alpabetic"""
print(mystring1.isalpha())

'''True'''



'''is alphanumeric'''
print(mystring1.isalnum())

'''True'''

'''is numeric'''

print(mystring1.isnumeric())

'''False'''





