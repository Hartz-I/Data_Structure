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
        
        
    def search(self, key):
        
        """
        Search for the first node that contains the data
        if not found returns a not found statement
        
        Takes O(n) runtime
        """
        
        current = self.head
        
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        
        return '<The value %d was not found in the linked list!>' %key
    
    
    def insert(self, data, index):
        
        """
        Inserts data to the specified index
        
        Insertion takes constant time
        getting to the index takes O(n) time
        
        Overall O(n)
        """
        
        current = self.head
        
        count = 0
        
        data = Node(data)
        
        while current:
            
            if index == 0:
                data.next_node = self.head
                self.head = data
                
                return None
            else:
                
                if count == index-1:
                    data.next_node = current.next_node
                    current.next_node = data
                    
                    return None
            
            current = current.next_node
            count +=1
            
    def remove(self, key):
        """
        Removes the first node that matches the key
        
        runtime O(n)
        """
        current = self.head
        
        if key == current.data:
            self.head = current.next_node
        
        while current:
            
            if key == current.data:
                prev.next_node = current.next_node
            
            prev = current
            current = current.next_node
            
        
        
    def __repr__(self) -> str:
        """
        returns a string of the linked list
        marks the head and tail
        """
        
        current = self.head
        
        text = ""
        
        while current != None:
            
            if current == self.head:
                text = text + "[Head:] " + str(current.data)
                
            elif current.next_node == None:
                text = text + " -> [Tail:] " + str(current.data)
                
            else:
                text = text + " -> " + str(current.data)
            
            current = current.next_node
            
        return text
    
    
l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.add(6)
l.add(7)
print(l.search(6))
l.insert(50, 6)
l.remove(5)
print(l)