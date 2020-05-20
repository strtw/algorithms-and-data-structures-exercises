class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


# Define a function outside of the class
def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here 
    newHead = Node(value)
    newHead.next = self.head #Set the head to be the next element after the prepend
    self.head = newHead #Then make the new prepend the head, this maintains the links. 
    self.head.previous = None #The first element doesn't have any previous elements. 
    self.length = self.length + 1
    if(self.length == 1):
        self.tail = self.head
        self.tail.previous = self.head

# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend

linked_list = LinkedList()

def append(self, value):#0(n) can't be used with append_quicker because it relies on a tail reference which this method doesn't set
    """ Append a value to the end of the list. """    
    # TODO: Write function to append here    
    if(self.head is None):
        self.head = Node(value)
        self.tail = self.head 
        print(self.head.value)
        return
    node = self.head
    print(node.value)
    while node.next:
        node = node.next
    print(node.value,linked_list.to_list())
    node.next = Node(value)
    




LinkedList.append = append
    
def append_quicker(self, value):#0(1), because we have a stored reference to the tail
    """ Append a value to the end of the list. """    
    # TODO: Write function to append here    
    if(self.head is None):
        self.head = Node(value)
        self.tail = self.head
    else:
       self.tail.next = Node(value)
       self.tail.next.previous = self.tail
       self.tail = self.tail.next
    self.length = self.length + 1
       

LinkedList.append_quicker = append_quicker

def search(self, value):#0(n)
    """ Search the linked list for a node with the requested value and return the node. """
    # TODO: Write function to search here
    node = self.head
    while(node):
        if(node.value == value):
            if(node.previous):print(node.previous.value, "Returned Search Previous Value")
            return node
        else:
            if(self.length > 1):  
                if(node.next):
                    node.next.previous = node
            node = node.next  
    return None   

LinkedList.search = search

def remove(self, value):
    """ Remove first occurrence of value. """
    # TODO: Write function to remove here
    nodeToRemove = linked_list.search(value)
    if(not nodeToRemove):
        return None
    self.length = self.length - 1
    if(self.head == self.tail):#Remove only element
        self.head = None
        self.tail = None
    elif(nodeToRemove == self.tail):
        nodeToRemove.previous.next = None #point the previous node to None
        self.tail = nodeToRemove.previous #Update the tail reference
        print(self.head.value, "head", self.tail.value, "Tail value")
    elif(nodeToRemove == self.head):
        print("Removing head",nodeToRemove.next.value)
        self.head = nodeToRemove.next
        print(self.head.value, "head", self.tail.value, "Tail value")
    else:
        nodeToRemove.previous.next = nodeToRemove.next #point the previous node to the node after current node
    
    
LinkedList.remove = remove 

def pop(self):
    """ Return the first node's value and remove it from the list. """
    # TODO: Write function to pop here
    if(self.length > 0):
        self.length = self.length - 1
    if(self.head is None):#Empty list
        return None
    else:
        node = self.head
        self.head = self.head.next #Sets head to next node, or none if there is no next node
        return node.value
    ''' First version, doesn't check for None first so had additional code. 
    firstNode = self.head
    if(self.head and self.head.next):
        self.head = self.head.next
    else:
        self.head = None
    if(self.length > 0):
        self.length = self.length - 1
    return firstNode
    '''


LinkedList.pop = pop


def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """
        
    # TODO: Write function to insert here  
    self.length = self.length + 1  
    node = self.head
    count = 0
    while(count <= pos):
        if(not node.next):
            currentNode = node
            node.next = Node(value)
            node.next.previous = currentNode
            return
        previousNode = node
        node = node.next
        count = count + 1
   # print(previousNode.value,"prev" )
   # print(node.value, 'cur')
    newNode = Node(value)
    newNode.previous = previousNode
   # print(newNode.value, 'newnode')
   # print(previousNode.next.value)
    previousNode.next = newNode
   # print(previousNode.next.value, 'new attached')
    newNode.next = node
   # print(newNode.next.value, "after new")

LinkedList.insert = insert


def size(self):
    return self.length

LinkedList.size = size

insert_list = LinkedList()
insert_list.append_quicker(0)
insert_list.append_quicker(1)
print(insert_list.to_list())
insert_list.insert(5,0)
insert_list.insert(10,100)
print(insert_list.to_list())

######  Test cases, start with empty list

linked_list.pop()
linked_list.append_quicker(5)
linked_list.pop()
linked_list.append_quicker(3)
linked_list.append_quicker(4)
linked_list.append_quicker(5)
linked_list.append_quicker(6)
linked_list.append_quicker(7)
assert linked_list.search(3).value == 3, f"list contents: {linked_list.to_list()}"
assert linked_list.search(100) == None, f"list contents: {linked_list.to_list()}" # No value in list
linked_list.prepend(2)
assert linked_list.to_list() == [ 2, 3, 4, 5, 6, 7], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
linked_list.insert(3,0)
linked_list.remove(5)
assert linked_list.to_list() == [2,3,4,6,7], f"list contents: {linked_list.to_list()}" 
linked_list.remove(4)#[3]
assert linked_list.to_list() == [2,3,6,7], f"list contents: {linked_list.to_list()}"
linked_list.remove(7)#[3]
assert linked_list.to_list() == [2,3,6], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)#[3]
assert linked_list.to_list() == [2,6], f"list contents: {linked_list.to_list()}"
linked_list.remove(2)#[3]
assert linked_list.to_list() == [6], f"list contents: {linked_list.to_list()}"
linked_list.remove(6)#[3]
assert linked_list.to_list() == [], f"list contents: {linked_list.to_list()}"
linked_list.append_quicker(4)
assert linked_list.to_list() == [4], f"list contents: {linked_list.to_list()}"
linked_list.insert(10,100)
assert linked_list.to_list() == [4,10], f"list contents: {linked_list.to_list()}"
print(linked_list.size(), linked_list.to_list())