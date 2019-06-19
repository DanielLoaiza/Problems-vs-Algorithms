#!/usr/bin/env python
# coding: utf-8

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
        pass
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        pass
        
    def suffixes(self, suffix = ''):
        suffixes = []
        def search_suffixes(word, currentNode):
            if(currentNode.is_word):
                suffixes.append(word)
            for k,v in currentNode.children.items():
                search_suffixes(word + k, v)
        
        search_suffixes("", self)
        return suffixes
        
class Trie():
    def __init__(self):
        self.root = TrieNode()
        pass

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True
        pass

    def find(self, prefix):
        current_node = self.root
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return None
        return current_node  
        pass

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[22]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');
