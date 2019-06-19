## Autocomplete with Tries
The implementation consists on using the find method to find the corresponding node to certain prefix, then starting from this node we need to iterate to every single node and return the ones that have is_word: true. the time complexity is O(n) and space complexity O(n) since we need to iterate on the entire sub-tree and store the results on an additional array
