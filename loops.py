# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 19:29:57 2017

@author: wilson
"""

'''LOOPS'''
people=['john','wilson','peter','james']

#for Loop
for i in people:
    print('Current person: '+i)
'''Iterate by seq index'''  
for i in range(len(people)):
    print('current person: '+ people[i])
    
  
'''Iterate using range'''
for i in range(1,11):
    print(i)

count=0;

while count<10:
    print('Count:', count)
    count +=1
    if count==5:
        break
    


   
"""










"""