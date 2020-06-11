"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        #pass
        # store old head
        old_head = self.head
        # store old tail
        old_tail = self.tail
        # create and store new node
        # if there's no head:
        if self.head == None:
            # create new node
            # set new node's next value to None
            # set new node's prev value to None
            new_node = ListNode(value, None, None)

            # set new node to be head
            self.head = new_node
            # set new tail to be tail
            self.tail = new_node
            # update length
            self.length = 1
        # otherwise
        else:
            # create new node
            # set new node's next value to old head node
            # set new node's prev to point to None
            new_node = ListNode(value, None, old_head)
            # set new node to be head
            self.head = new_node
            # set old node's prev to point to new node
            old_head.prev = new_node
            # increment the length
            self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # pass
        # store old head 
        old_head = self.head
        # if the length is 1 (meaning the node is both the head and tail)
        if self.length == 1:
            # update the head to be None
            self.head = None
            # update the tail to be None
            self.tail = None
            # update length to be 0
            self.length = 0
            return old_head.value
        # otherwise:
        else:
            # set head to be the next value (that the old head was pointing to)
            self.head = old_head.next
            # update new head's prev pointer to be None (instead ot the old head)
            self.head.prev = None
            # decrement length
            self.length -= 1
            return old_head.value
        ###### things I forgot in my planning: 
            # returning the old value
            # storing the old head

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # pass
        # Store old tail
        old_tail = self.tail
        # If the tail is None
        if self.tail == None:
            # create a new node from the 'value'
            new_node = ListNode(value, None, None)
            # set head to be the new node
            self.head = new_node
            # set tail to be the new node
            self.tail = new_node
            # update length to be 1
            self.length = 1
        # Otherwise:
        else:
            # create a new node from the 'value'
            new_node = ListNode(value, old_tail, None)
            # set the tail to be the new node
            self.tail = new_node
            # set old tail's next to point to the new node (instead of None)
            old_tail.next = new_node
            # set new node's prev. to point to the old tail
            # update length to increment
            self.length += 1
        ####### things I forgot in my planning:
            # I forgot that setting the prev would be done when creating the node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # pass
        # store old tail
        old_tail = self.tail
        # if the length is 1
        if self.length == 1:
            # 
            self.head = None
            self.tail = None
            self.length = 0
            return old_tail.value
        else:
            self.tail = old_tail.prev
            self.tail.next = None
            self.length -= 1
            return old_tail.value
        ####### things I forgot in my planning:
            # I forgot to set the head and tail (in "add_to_tail") to be the new node (instead of None)
            # forgot to return the value of the tail in "remove_from_tail"

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # pass
        # call "add_to_tail" method, with node passed in
        self.add_to_head(node.value)
        # call "delete" method, with node passed in
        self.delete(node)
        ######### Things I forgot in my planning:
            # forgot that I need to pass in the VALUE of the node for add_to_head method

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # pass
        # call "add_to_tail" method, with node's VALUE passed in
        self.add_to_tail(node.value)
        # call "delete" method with node passed in
        self.delete(node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # pass
        # store the node
        stored_node = node
        # if length is 0:
        # if self.length == 0:
        #     # do nothing
        #     return
        # # if length is 1: 
        # elif length == 1:
        #     # remove from head
        #     node.remove_from_head()

        if node.prev == node.next:
            # call remove_from_head
            # node.remove_from_head()
            self.head = None
            self.tail = None
            self.length = 0
            return
        # if node is head:
        elif node.prev == None:
            node.next.prev = None
            self.head = stored_node.next
            self.length -= 1
        # if node is tail:
        elif node.next == None:
            # call remov_from_tail
            # node.remove_from_tail()
            node.prev.next = None
            self.tail = stored_node.prev
            self.length -= 1
        # otherwise:
        else:
            # node's prev node's next pointer needs to now point to node's next 
            # stored_node.prev.next = stored_node.next
            # node's next node's prev pointer needs to now point to node's prev
            # stored_node.next.prev = stored_node.prev
            node.delete()
            self.length -= 1
        ######## Things I forgot:
            # forgot that the node itself doesn't have a "length"
            # forgot that the DoublyLinkedList methods can't be used here
            # I think I got confused about the class methods since it's early in the morning

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # pass
        # max_so_far = None
        # but we don't really want None, because we can't compare that to a number
        max_so_far = self.head.value
        # we want to traverse until the "next" pointer is None
        # can't use a for loop because we don't know the length
        # so we need a while loop
        # set current node
        current_node = self.head
        # while current_node.next != None:
        # with above having the next property as a condition, we were stopping just before that last node, so when it got to 100, it said "ok, awesome, the next is None, so I don't need to compare that value to the max"
        while current_node != None:
            if  max_so_far < current_node.value:
                max_so_far = current_node.value
            current_node = current_node.next
            # print(current_node.value)
        return max_so_far