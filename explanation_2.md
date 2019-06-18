## Search in a Rotated Sorted Array

The idea here is to find the rotation first to know where should the search go to, in order to accomplish this we compare the current pivot (mid)  with the lowest and the highest elements, if lowest is higher than the pivot then there is a rotation. time complexity is O(logn)
