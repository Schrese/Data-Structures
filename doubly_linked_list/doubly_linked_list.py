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
        # pass
        # store the current head
        old_head = self.head
        old_tail = self.tail
        # create a new head node
        new_head = ListNode(value, None, old_head)
        # use insert before to but the new head in front of the old head
        new_head.insert_before(old_head)
        # update the head to be the new head node
        # self.head = new_head => if this isn't in a conditional, it will fail for if there isn't a tail
        # self.length += 1 => if this isn't in a conditional, it will fail for if there isn't a tail
        if self.tail.value == self.head.value:
            self.head = new_head
            self.tail = new_head
            self.length += 1
        # increment the length of the list
        else:
            self.head = new_head
            self.length += 1
            
        # print(self.length)
        # print(self.head.value)


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # pass
        old_head = self.head
        # Sooooo.... turns out I don't need to check the value of the head... Interesting
        # if self.head.value == 1: 
        #     self.head.next = None
        #     # self.tail.value = None
        #     # print("hello")
        #     # return None
        if self.tail.value == self.head.value:
            self.tail.delete()
            self.head.delete()
            self.length -= 1
        else:
            self.head.delete()
            self.length -= 1
        
        print(self.length)
        print(self.head.value, "something")

    # def remove_from_head(self):
    #     # pass
    #     old_head = self.head
    #     if self.head.value == 1:
    #         self.head.next = None
    #         # self.tail.value = None
    #         # print("hello")
    #         # return None
    #     elif self.tail.value == self.head.value:
    #         self.tail.delete()
    #         self.head.delete()
    #         self.length -= 1
    #     else:
    #         self.head.delete()
    #         self.length -= 1
        
    #     print(self.length)
    #     print(self.head.value, "something")

    # Below was my original idea, trying something new above
        # old_head = self.head
        # old_tail = self.tail
        # print(self.head.value)
        # print(self.tail.value)
        # print(self.length)
        # if self.head.value == 1 and self.tail.value == 1:
        #     self.head = old_head
        #     self.tail = old_tail
        #     self.length = self.length
        # else:
        # # if self.head != 0:
        #     self.head.delete()
        #     self.length -= 1
        #     return old_head
        

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # pass
        # Store the current head and tail
        old_head = self.head
        old_tail = self.tail
        # Create a new node and set it to a new tail variable
        new_tail = ListNode(value, old_tail, None)
        # insert the new tail after the previous tail
        new_tail.insert_after(old_tail)
        # Interesting... I don't need a conditional here?
        # conditional to check that the head and tail aren't the same
        # if self.tail.value == 1:
        #     self.head = new_tail
        #     self.tail = new_tail
        #     self.length += 1
        # if they aren't, increment the length of the list, and set the new tail
        # else:
        self.tail = new_tail
        self.length += 1




    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        pass
        # Store current tail
        current_tail = self.tail
        # check that the head and tail don't have the same values
        if self.head.value == self.tail.value:
            self.head.next = None
            self.head.prev = None
            # if they do, then there will no longer be a head or a tail, and the length will be 0
        # otherwise delete the tail and decrement by 1
        else:
            self.tail.delete()
            current_tail.prev.next = None
            self.length -= 1 

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        pass
