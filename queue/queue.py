"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# Pretty much the same as the stack, but just in reverse orders for the dequeue

# For using the Stack class on the Queue, I would assume that I would need to do some reversal of orders and then use the stack methods

# from singly_linked_list import LinkedList

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):
#         # pass
#         return self.size

#     def push(self, value):
#         # pass
#         self.size += 1
#         return self.storage.add_to_tail(value)

#     def pop(self):
#         # pass
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.remove_tail()


# class Queue(Stack):
#     def __init__(self, size, storage):
#         super().__init__(size, storage)
    
#     def enqueue(self, value):
#         storage_reverse = self.storage.reverse()
#         print(storage_reverse)




from singly_linked_list import LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        # pass
        return self.size

    def enqueue(self, value):
        # pass
        self.size += 1
        return self.storage.add_to_tail(value)

    def dequeue(self):
        # pass
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()


# class Queue:
#     def __init__(self, storage=[]):
#         self.size = 0
#         self.storage = storage
    
#     def __len__(self):
#         # pass
#         if self.size == 0:
#             return 0
#         else: 
#             return self.size

#     def enqueue(self, value):
#         # pass
#         new_list = self.storage.insert(0, value)
#         self.size += 1
#         return new_list

#     def dequeue(self):
#         # pass
#         if self.size > 0:
#             something = self.storage.pop(self.size-1)
#             self.size -= 1
#             return something