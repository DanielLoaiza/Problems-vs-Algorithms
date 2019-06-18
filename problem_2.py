#!/usr/bin/env python
# coding: utf-8

# In[35]:


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    max = len(input_list) -1
    min = 0
    
    rotatedIndex = -1
    
    while(min <= max):
        mid = (max + min) // 2
        if(number == input_list[mid]):
            return mid
        else:
            #check two possible pivots
            left_max = mid
            left_mid = (left_max + min) //2
            left_element = input_list[left_mid]
            
            right_min = mid
            right_mid = (right_min + max)//2
            right_element = input_list[right_mid]
            
            # there is an inversion
            if(left_element > right_element):
                right_minimum =  right_element - (right_mid -  mid) + 1
                right_max = right_element + (max - right_mid)
                
                if(is_between(number, right_minimum, right_max)):
                    min = mid + 1
                else:
                    max = mid - 1
                    
            else:
                #normal search
                if(number > input_list[mid]):
                    min = mid + 1
                else:
                    max = mid - 1
    return -1   
    pass

def is_between(number, min, max):
    return number >= min and number <= max

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")
        
test_function([[5, 6, 7, 0, 1, 2, 3, 4], 4])
test_function([[4, 5, 6, 7, 0, 1, 2], 4])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

