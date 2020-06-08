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
class Stack:
    def __init__(self, storage=[]):
        self.size = 0
        self.storage = storage

    def __len__(self):
        # pass
        # We'll use the "len()" List method 
        # self.size = len(self.storage)
        # Return "0" for an empty array
        if self.size == 0:
            return 0
        # Otherwise, return the length of the array
        else:
            return self.size

    def push(self, value):
        # pass
        # We'll use the "append()" List method
        new_list = self.storage.append(value)
        self.size += 1
        return new_list
        # We shouldn't need conditionals here since if there's nothing in the stack, it will add to the end, and if there is something in the stack, then it'll still add to the end

    def pop(self):
        # pass
        # We'll use the "pop()" List method with no parameters passed in
        if self.size > 0:
            # print(self.size)
            # val = self.storage[self.size]
            self.size -= 1
            return self.storage.pop()

            # print(val)

            # return something
        # if self.size == 0:
        #     return 0
        # else:
        #     self.storage.pop()
        #     self.size -= 1

        # This already returns the element that has been removed, and by default will remove the last element in the list