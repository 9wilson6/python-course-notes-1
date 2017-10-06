# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:57:30 2017

@author: wilson
"""
#impotr entire module
import greet
#import  a specific element
from greet import sayGoodbye
"""IMPORTING ANOTHER APP TO CURRENT APP"""
greet.sayHello('wilson')

'''
Hello  wilson From greetings module
Hello  james From greetings module
'''
sayGoodbye('gatheru')
'''
Hello  wilson From greetings module
Goodbye  gatheru From greetings module
'''