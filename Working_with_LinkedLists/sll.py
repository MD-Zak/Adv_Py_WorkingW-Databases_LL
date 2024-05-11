
"""Creating the abstract Singly LinkedList  data type"""
class SLLNode:
    
    def __init__(self, data):
        self.data = data
        self.next = None # at first the next attribute of the node points to None, thus it is a empty LL at first.
        #Note: LL can be recursive or empty, any one of the two at all times.*

    # we need a representation of the SLLNode obj. whenever we return it on the prompt.
    def __repr__(self):
        return f"<SLLNode obj w/ data: {self.data}>"

    def get_data(self):
        """Returns the self.data attribute of the SLLNode object"""
        return self.data

    def set_data(self, new_data):
        """Adds/stores the parameter, new_data as the new self.data attribute to the SLLNode object"""
        self.data = new_data

    def get_next(self):
        """This method will allow us to transverse the SLL to get to the next SLL node.
        this should return the next node address, i.e, this is essentially a pointer, 
        that as the memory address of the next node."""
        # a node is part of a LinkedList data structure.
        return self.next

    def set_next(self, new_next):
        """Here we will set the next pointer, that points to another node in the LinkedList.
        i.e., using the self.next attribute."""
        self.next = new_next

class SLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"<SLL object w/ head = {self.head}>"

    def is_empty(self):
        """Checks if the sll is empty"""
        return self.head is None
    
    def add_front(self, new_data):
        """Adds a node to the head from front"""
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp
        # self.head = SLLNode(new_data).set_next(self.head) # Here the new value points to the none type and
                                                            # finally becomes the none type.
    
    def size(self):
        """Returns the size of sll
        By traversing the nodes of the sll.

        The time complexity is O(n) as the worst case scenario is reading all nodes."""
        size = 0        
        if self.head is None:
            return size

        current = self.head
        while current is not None:
            size += 1
            current = current.get_next()
        return size
    
    def search(self, data):
        """Searches for a data in the sll

        The time complexity is O(n) as the worst case scenario is reading all nodes."""

        if self.head is None:
            return "Linked list is empty, there are 0 nodes to search."
        
        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True # An improvement would be to return the index of the node.
            else:
                current = current.get_next()
        return False
    
    def remove(self, data):
        """Removes a data from the sll
                
        The time complexity is O(n) as the worst case scenario is reading all nodes."""

        # if self.head is None:
        #     return 'Linked list is empty, there is no data to remove.'

        # current = self.head
        # while current is not None:
        #     if current.get_data() == data:
        #         temp = current
        #         current.set_data(None)
        #         return f'Data removed', self.size()
        #     else:
        #         current = current.get_next()
        # return "Entered data not present in the SLL."

        # The above code does not really unlink the SLL, after search. It counts the
        # remove_data converted to None also.
        # Thus, in order to essentially remove the data, we must change the links.
        print(f"\n Nodes in LL before removal: ",self.size())
        if self.head is None:
            return "LinkedList empty, no data to search."

        found = False
        previous = None
        current = self.head
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() == None:
                    return "Data searched does not exist."
                else:
                    previous = current
                    current = current.get_next()
                
        if previous is None:
            self.head = current.get_next()            
        else:
            previous.set_next(current.get_next())
        if found:
            return print(f"\n Nodes in LL after removal: ",self.size())


