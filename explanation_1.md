## Finding the Square Root of an Integer

This problem is solved using binary search, starting from 0 to number / 2 (since its the max number that can be the square of the target)
depending if the current number multiplied by itself its higher or lower than the target, min and max are changed. this algorithm is solved on O(logn) and space complexity O(1) since no additional data storage is needed
