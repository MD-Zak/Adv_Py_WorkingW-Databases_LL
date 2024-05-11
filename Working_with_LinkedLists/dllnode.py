
"""Creating the abstract Singly LinkedList data type"""
class DLLNode:
    
    def __init__(self, data):
        self.data = data
        self.next = None # at first the next attribute of the node points to None, thus it is a empty LL at first.
        #Note: LL can be recursive or empty, any one of the two at all times.*
        self.previous = None

    # we need a representation of the DLLNode obj. whenever we return it on the prompt.
    def __repr__(self):
        return f"<DLLNode object w/ data: {self.data}>"

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

    def get_previous(self):
        """Returns the self.previous attribute"""
        return self.previous

    def set_previous(self, new_previous):
        """Replaces the self.previous attribute with the new_previous parameter."""
        self.previous = new_previous