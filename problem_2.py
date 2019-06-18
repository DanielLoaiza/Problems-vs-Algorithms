#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Returns index of key in arr[l..h] if key is present, 
# otherwise returns -1 
def rotated_array_search (arr, number):
    def search (arr, low, high, key):
        if low > high: 
            return -1
      
        mid = (low + high) // 2
        if arr[mid] == key: 
            return mid 
  
        # If arr[l...mid] is sorted  
        if arr[l] <= arr[mid]: 
  
            # As this subarray is sorted, we can quickly 
            # check if key lies in half or other half  
            if key >= arr[l] and key <= arr[mid]: 
                return search(arr, l, mid-1, key) 
            return search(arr, mid+1, h, key) 
  
        # If arr[l..mid] is not sorted, then arr[mid... r] 
        # must be sorted 
        if key >= arr[mid] and key <= arr[h]: 
            return search(arr, mid+1, h, key) 
        return search(arr, l, mid-1, key)
    
    return search(arr, 0, len(arr)-1 , number)

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
test_function([[7, 8, 10, 12, 1, 2, 4, 6], 10])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

