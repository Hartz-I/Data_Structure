class Node:
    
    """
    An object for storing a single node of a linked list
    Models two attributes -  data and a link to the next node of the list
    """
    
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
        
    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data
    
class LinkedList:
    """
    Singly Linked List
    """
    
    def __init__(self) -> None:
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Return the number of nodes in the list
        Takes Linear Time
        """
        current = self.head
        count = 0
        
        while current != None:
            count += 1
            current = current.next_node
            
        return count
        
    def add(self, data):
        """
        adds a new node containing data at the head of the list
        this operation takes constant time
        """
        
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node