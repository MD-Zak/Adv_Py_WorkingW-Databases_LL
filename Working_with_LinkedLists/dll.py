
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
        """Returns the self.data attribute of the DLLNode object"""
        return self.data

    def set_data(self, new_data):
        """Adds/stores the parameter, new_data as the new self.data attribute to the DLLNode object"""
        self.data = new_data

    def get_next(self):
        """This method will allow us to transverse the DLL to get to the next DLL node.
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

class DLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return f'<DLL obj w/ head: {self.head}>'

    def is_empty(self):
        return self.head is None
    
    def size(self):
        """Returns the size of dll
        By traversing the nodes of the dll.

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
        """Searches for a data in the dll

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

    def add_front(self, data):
        temp = DLLNode(data)
        temp.set_next(self.head) # we are moving the new node, temp to the first pos, by pushing the node pointed by the attribute self.head
        if self.head is not None: # As self.previous is set to None in the dunder init, we need to make sure the LL is not empty.
            self.head.set_previous(temp) # 
        self.head = temp # this will make the node attribute, self.head the latest node on the LL for future cux.

    def remove(self, data):
        """Removes a data from the dll
        
        The time complexity is O(n) as the worst case scenario is readingx all nodes."""

        if self.head is None:
            return "LinkedList is empty, no nodes to search."

        found = False
        current = self.head
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "Item to be removed is not in the LinkedList."
                else:
                    current = current.get_next()

        if current.previous is None:
            self.head = current.get_next()
        else:
            current.previous.set_next(current.get_next())
            if current is not None:
                current.next.set_previous(current.get_previous())
            else:
                print('current was None.')
