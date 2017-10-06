# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:58:43 2017

@author: wilson
"""

#CLASSES AND OBJECTS
class Person:
    
    __name=''
    __email=''
    def __init__(self, name, email):
        self.__name= name
        self.__email= email
        
    def set_name(self, name):
        
        self.__name=name
    def getName(self):
        return self.__name
    
    
    def set_email(self, email):
        self.__email=email
        
    def getEmail(self):
        return self.__email
    def toString(self):
        return '{} can be contacted at {}'.format(self.__name, self.__email)


wilson= Person('willie', 'gatheru@gmail.com')

#print(wilson.getName())
#print(wilson.getEmail())
#print(wilson.toString())

"""inheritance"""

class Customer(Person):
    __balance = 0
    
    def __init__(self,name, email, balance):
        self.__name=name
        self.__email=email
        self.__balance=balance
        
        super(Customer, self).__init__(name,email)
    def set_balance(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def toString(self):
        return '{} has a balance of {} and can be contacted at {}'.format(self.__name, self.__balance, self.__email)
g=Customer('wilson' , 'gatheruwilson@gmail.com',200)

print(g.toString())








 


















