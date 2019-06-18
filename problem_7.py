#!/usr/bin/env python
# coding: utf-8

# In[21]:


from enum import Enum

class HandlerType(Enum):
    NOT_FOUND = 1
    FOUND = 2
#Handler
class Handler:
    def __init__(self, name = "",type = HandlerType.NOT_FOUND):
        self.type = type
        self.name = name
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler = Handler()):
        self.root = RouteTrieNode(handler)
        # Initialize the trie with an root node and a handler, this is the root path or home page node

    def insert(self, path, handler_name):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for segment in path:
            if segment not in current_node.children:
                current_node.insert(segment)
            current_node = current_node.children[segment]

        current_node.handler = Handler(handler_name, HandlerType.FOUND)
        pass

    def find(self, path):
        current_node = self.root
        for segment in path:
            if segment in current_node.children:
                current_node = current_node.children[segment]
            else:
                return None
        return current_node

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = Handler()):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path, handler = Handler()):
        self.children[path] = RouteTrieNode(handler)

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(Handler(root_handler, HandlerType.FOUND))
        self.not_found_handler = Handler(not_found_handler, HandlerType.NOT_FOUND)

    def add_handler(self, path, handler_name):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.route_trie.insert(self.split_path(path), handler_name)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if(path == "/"):
            return self.route_trie.root.handler.name
        
        path_segments = self.split_path(path)
        node = self.route_trie.find(path_segments)
        
        if node is None or node.handler.type is HandlerType.NOT_FOUND:
            return self.not_found_handler.name
        else:
            return node.handler.name
        
            
            


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        final_path = path
        if(final_path.endswith("/")):
            final_path = final_path[:-1]
            
        return final_path.split("/")


# In[24]:


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

