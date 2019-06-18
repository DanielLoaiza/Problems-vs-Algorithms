## Autocomplete with Tries
The implementation consists on using the find method to find the corresponding node to certain prefix, then starting from this node we need to iterate to every single node and return the ones that have is_word: true. the time complexity is O(n)
