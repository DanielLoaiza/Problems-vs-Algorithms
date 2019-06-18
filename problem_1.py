#!/usr/bin/env python
# coding: utf-8

# In[19]:


import math

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if(number == 0):
        return 0
    if(number == 1):
        return 1
    
    divider = math.floor(number / 2)
    minInterval = 0
    maxInterval = divider
    while(minInterval < maxInterval):
        result = divider * divider
        if(result > number):
            maxInterval = divider
            divider = math.floor((minInterval + maxInterval) / 2)
        elif(result < number):
            minInterval = divider
            if(maxInterval - minInterval == 1):
                return minInterval
            divider = math.floor((minInterval + maxInterval) / 2)
        elif(number % result == 0):
            return divider
            
    pass

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

