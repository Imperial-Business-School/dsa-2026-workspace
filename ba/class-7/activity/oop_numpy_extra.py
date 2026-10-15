
# Implement the ListQueue() class using python lists.

class ListQueue(object):
    """ 
    Queue using list
    Supports inserting and deleting nodes
    """
    def __init__(self):
        """Initialise queue as list"""
        self.items=[]

    def is_empty(self):
        """
        Checks if queue is empty
        """
        return len(self.items) == 0      

    def enqueue(self, item): 
        """ 
        Insert an element into the end of the queue (list)
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove the first element of the queue, return it
        """
        return self.items.pop(0) 


def test_listqueue():
    """
    Tests for the ListQueue() class.
    
    Examples:
    >>> LQ = ListQueue()
    >>> LQ.enqueue(2)
    >>> LQ.enqueue(1)
    >>> print(LQ.items)
    [2, 1]
    >>> x = LQ.dequeue()
    >>> print(LQ.items)
    [1]
    >>> LQ = ListQueue()
    >>> A = [135, 891, 886, 537, 253, 6, 635, 577, 331, 192]
    >>> if LQ.is_empty():
    ...     for i in A: 
    ...         LQ.enqueue(i)
    >>> for i in range(int(len(LQ.items)/2)):
    ...     z = LQ.dequeue()
    >>> print(LQ.items)
    [6, 635, 577, 331, 192]
    """
    # DON'T EDIT THIS FUNCTION
    pass
    

# Implement the Queue() class using the Node() class.

class Node(object):
    """ 
    Node class: contains unspecified data in stuff and link to next Node
    """
    def __init__(self, stuff=None, next=None):
        self.stuff = stuff
        self.next  = next

    def __str__(self):
        return str(self.stuff) 

 
class Queue(object):
    """ 
    Queue using linked Nodes
    Supports inserting and deleting nodes
    """
    def __init__(self):
        """ Initialise queue. Keep track of both first and last node for fast operations"""
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, stuff):
        """ 
        Insert a Node into end of queue
        """
        node = Node(stuff)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            last = self.last
            last.next = node
            self.last = node
        self.length += 1 # increase queue length

   
    def dequeue(self):
        """
        Removes first node of the queue and returns it
        """

        removed_contents = self.first.stuff
        self.first = self.first.next # update the first node
        self.length -= 1 # decrease queue length
        if self.length == 0:
            self.last = None
        return removed_contents

            
    def is_empty(self):
        """
        Checks if queue is empty
        """
        return self.length == 0
    
    def __str__(self):
        """
        Return the queue elements as a string separated by spaces (see example below)
        """
        #Start at head
        s = []
        current_node = self.first
        while current_node is not None:
            s.append(str(current_node.stuff))
            current_node = current_node.next
        return " ".join(s) + " "
            
    def __len__(self):
        return self.length


def test_queue():
    """
    Tests for the Queue() class.
    
    Examples:
    >>> Q = Queue()
    >>> Q.enqueue(2)
    >>> Q.enqueue(1)
    >>> str(Q)
    '2 1 '
    >>> x = Q.dequeue()
    >>> str(Q)
    '1 '
    >>> Q = Queue()
    >>> A = [135, 891, 886, 537, 253, 6, 635, 577, 331, 192]
    >>> if Q.is_empty():
    ... 	for i in A: 
    ... 		Q.enqueue(i)
    >>> for i in range(int(len(Q)/2)):
    ...     z = Q.dequeue()
    >>> str(Q)
    '6 635 577 331 192 '
    """
    pass
    # DON'T EDIT THIS FUNCTION



