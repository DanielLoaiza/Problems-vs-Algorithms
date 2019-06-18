#!/usr/bin/env python
# coding: utf-8

# In[28]:


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    rearranged_items = []
    items = mergesort(input_list)
    mid = len(items) // 2
    if(len(items) % 2 == 0):
        mid = (len(items) // 2) -1
    concatenated_number = ""
    for index, element in enumerate(items):
        concatenated_number = int(str(concatenated_number) + str(element))
        if(index == mid):
            rearranged_items.append(concatenated_number)
            concatenated_number = ""
        elif index == len(items)- 1:
             rearranged_items.append(concatenated_number)
    return rearranged_items
    pass

def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

    
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")
        
test_function([[1, 2, 3, 4, 5], [543, 21]])
test_case = [[4, 6, 2, 5, 9, 8], [986, 542]]
test_function(test_case)
test_function( [[8,4, 6, 2, 5, 0, 9, 8, 3, 1], [98865, 43210]])

