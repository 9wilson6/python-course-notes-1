# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 19:08:42 2017

@author: wilson
"""

'''CONDITIONALS'''
x=14
if x < 6:
    print("this is true")
'''IF ELSE'''
if x < 2:
    print('this is True')
else:
    print('this is purely false')
    
'''Elif'''
color='red'
if color=='red':
    print("color is Red")
elif color=='blue':
    print('Color is Blue')
else:
    print('Color is not Red Or Blue')
    
    
"""NESTED IF STATEMENTS"""    

if color=='green':
    if x< 10:
        print('color is green and X is less than 10')
    elif x > 10:
        print('color is green but x is not less than 10')

else:
    print('Color is not green nor is X less than 5')


"""LOGICAL OPERRATORS"""

if color=='red' and x < 10:
    print('color is red and x is less 10')
elif color=='red' and x >10:
    print("color is red but x is not less than 10")
elif color!='red' and x<10:
    print("color is not Red but x is less than 10")
else:
    print("Color is not red nor is x < 10")
''''''

 

   
    
    
    
    
    