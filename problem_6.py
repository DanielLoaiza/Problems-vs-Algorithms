#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys
def get_min_max(ints):
    min = sys.maxsize
    max = -sys.maxsize -1
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    for number in ints :
        if(number < min):
            min = number
        if(number > max):
            max = number
    
    return min,max
    pass

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
