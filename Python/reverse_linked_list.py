class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])

def reverse_list(list):
        newList = LinkedList()
        previousNode = None
        for value in list:
            newNode = Node(value)
            newNode.next = previousNode#Set the reference to be the node to the right
            previousNode = newNode
        newList.head = previousNode#The last node in the first list
        return newList

myList = LinkedList()
myList.append(1)
myList.append(2)
myList.append(3)

reverse_list(myList)