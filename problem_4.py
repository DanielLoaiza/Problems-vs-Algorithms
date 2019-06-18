#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Function to sort array 
def sort_012(a): 
    low = 0
    high = len(a) - 1
    index = 0
    while index <= high: 
        if a[index] == 0: 
            a[index] = a[low]
            a[low] = 0 
            low = low + 1
            index = index + 1
        elif a[index] == 1: 
            index = index + 1
        else: 
            a[index] = a[high]
            a[high] = 2 
            high = high - 1
    return a 
    pass

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

