"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # pass
        # if value is greater than self.value
        if value >= self.value:
            # if self.right has a node
            if self.right:
                # set new self to that node and re-run this method
                self.right.insert(value)
            # otherwise
            else:
                # create a new node there
                self.right = BSTNode(value)
        # if value is less than self.value
        else:
            # if self.left has a node
            if self.left:
                # set new self to that node and re-run this method
                self.left.insert(value)
            # otherwise
            else:
                # create a new node there
                self.left = BSTNode(value)
        # print('inserted', value)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # pass
        # if the target is equal to the value of self
        if target == self.value:
            # return true
            return True
        # if the target is greater than the value of self
        elif target > self.value:
            # check to see if there's a node to the right of self
            if self.right:
                # if there is, then set self to that node and re-run this method
                return self.right.contains(target)
            # otherwise 
            else:
                # return False
                return False
        # if the target is less than the value of self
        elif target < self.value:
            # check to see if there's a node to the left
            if self.left:
                # if there is, then selt self to that node and re-run this method
                return self.left.contains(target)
            # otherwise
            else:
                # return False
                return False
        # otherwise, if there just isn't a node to check against,
        else: 
            # return false
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # pass
        # # Store the current value of self
        # current_self = self.value
        # print(self.value)
        # I think that the bottom-rightmost node will always hold the largest value
        # if there is a node to the right of self
        if self.right:
            # set that node's value to self and re-run the method
            return self.right.get_max()
        # otherwise
        else:
            # return the value of self
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
