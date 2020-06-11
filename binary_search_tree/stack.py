"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# The difference seems to be that if we are able to make our own linked list, then we know exactly what will get returned to us. It also makes conditional writing a bit easier (because it removes the need for several nested conditionals). While it seems like it'd be easier to control your own code if I write my own list methods, I think the downside is both time, as well as (maybe???) future implementation (it seems like at a certain point, when considering scalability, that there might be more issues further down the line that the built-in methods might not have)? But I'm really not sure
from singly_linked_list import Node, LinkedList

# BELOW IS WITH THE SINGLY LINKED LIST

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        # pass
        return self.size

    def push(self, value):
        # pass
        self.size += 1
        return self.storage.add_to_tail(value)

    def pop(self):
        # pass
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_tail()

# BELOW IS WITH PLAIN PYTHON LISTS 

# class Stack:
#     def __init__(self, storage=[]):
#         self.size = 0
#         self.storage = storage

#     def __len__(self):
#         # pass
#         # We'll use the "len()" List method 
#         # self.size = len(self.storage)
#         # Return "0" for an empty array
#         if self.size == 0:
#             return 0
#         # Otherwise, return the length of the array
#         else:
#             return self.size

#     def push(self, value):
#         # pass
#         # We'll use the "append()" List method
#         new_list = self.storage.append(value)
#         self.size += 1
#         return new_list
#         # We shouldn't need conditionals here since if there's nothing in the stack, it will add to the end, and if there is something in the stack, then it'll still add to the end

#     def pop(self):
#         # pass
#         # We'll use the "pop()" List method with no parameters passed in
#         if self.size > 0:
#             # print(self.size)
#             # val = self.storage[self.size]
#             self.size -= 1
#             return self.storage.pop()

#             # print(val)

#             # return something
#         # if self.size == 0:
#         #     return 0
#         # else:
#         #     self.storage.pop()
#         #     self.size -= 1

#         # This already returns the element that has been removed, and by default will remove the last element in the list