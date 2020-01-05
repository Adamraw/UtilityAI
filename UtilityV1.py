#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 19:11:06 2019

@author: ragab
"""

import matplotlib.pyplot as plt
import numpy as np
import PyQt5
import sys
import re
import operator


modulename = 'PyQt5'
if modulename not in sys.modules:
    print('You have not imported the {} module'.format(PyQt5))
else:
    print('PyQt5 imported')
    


class Utility_Function:
    def __init__(self,**kwargs):
        for key, value in kwargs.items():
            setattr(self, key, float(value))

    def Create_Math_Function(self,x = input()):
      self.Math_Function = re.sub(r"((?:\d+)|(?:[a-zA-Z]\w*\(\w+\)))((?:[a-zA-Z]\w*)|\()", r"\1*\2", x)


#we need a decorator here (maybe)
    def Evaluate_Math_Function(self):
      Result = eval(self.Math_Function,{'__builtins__': None},vars(self))
      return Result

#UNDERPROGRESS
    def Evaluate_Math_Function1(self,localvar):
      Result = eval(self.Math_Function,{'__builtins__': None},localvar )
      return Result
    
    def Graph_Function(self):
      xaxis = []
      yaxis = []
      for i in range(100):
        xaxis.append(i)
      for i in xaxis:
        localvar = vars(self)
        localvar["x"] = i
        localvar["y"] = i
        localvar["z"] = i
        #function eval1 not just eval
        yaxis.append(self.Evaluate_Math_Function1(localvar))
      plt.plot(xaxis,yaxis)
      plt.show()





#this works
class Selector_Object:
   cached_dictionary = {}
   def __init__(self,**kwargs):
     for key,value in kwargs.items():
       if isinstance(value, Utility_Function):
         setattr(self,key, value)
      


   def evaluate_function_scores(self):
     for key,value in vars(self).items():
       #print(key,value.Evaluate_Math_Function())
       self.cached_dictionary[key] = value.Evaluate_Math_Function()
  

   def s_scores(self):
     cach_dic = self.cached_dictionary
     sorted_dic = sorted(cach_dic, key = cach_dic.get, reverse = True )
     print(sorted_dic) 



  





Test = Utility_Function(x = 2, y = 22, z = 12)

#Raw = Utility_Function(x = 5, y = 11, z = 12)

#Jaw = Utility_Function(x = 3)

Test.Create_Math_Function()
#Raw.Create_Math_Function()
#Jaw.Create_Math_Function()

print(vars(Test))
#print(Test.Math_Function)

#Test.Evaluate_Math_Function()
#Raw.Evaluate_Math_Function()
#Jaw.Evaluate_Math_Function()

#Test_Selector = Selector_Object(U1 = Test , U2 = Raw, U3 = Jaw)
#Test_Selector.evaluate_function_scores()
#Test_Selector.s_scores()


Test.Graph_Function()
