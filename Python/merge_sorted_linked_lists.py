# Helper code

# A class behaves like a data-type, just like an int, float or any other built-in ones. 
# User defined class
class Node:
    def __init__(self, value): # <-- For simple LinkedList, "value" argument will be an int, whereas, for NestedLinkedList, "value" will be a LinkedList
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)
    
# User defined class
class LinkedList: 
    def __init__(self, head): # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head
    
    '''
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    '''
    def append(self, value):
        
        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return
        
        # Create a temporary Node object
        node = self.head
        
        # Iterate till the end of the currrent LinkedList
        while node.next is not None:
            node = node.next
        
        # Append the newly creataed Node at the end of the currrent LinkedList
        node.next = Node(value)

        
    '''We will need this function to convert a LinkedList object into a Python list of integers'''
    def to_list(self):
        out = []          # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object
        
        while node:       # <-- Iterate untill we have nodes available
            out.append(int(str(node.value))) # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            node = node.next
        
        return out

def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    '''
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    '''
    node1 = list1.head
    node2 = list2.head
    #Set the first node in newList
    if(node1.value > node2.value):
        newList = LinkedList(Node(node2.value))
        node2 = list2.head.next
    else:
        newList = LinkedList(Node(node1.value))
        node1 = list1.head.next

    
    while node2 or node1:#While either node has a next node
        #Find the lesser node value from a list and append it to newList, and advance the node of this list
        if(not node1 or node1.value  > node2.value):#If node1 doesn't exist (which means we've already added all list1's values) or its value is greater than node2
            newList.append(node2.value)#Append node2 value to the new list
            node2 = node2.next #Advance the node. If it doesn't exist, then on the the next while loop check it will not enter the loop
        else:
            newList.append(node1.value)
            node1 = node1.next
    return newList

# First Test scenario
''' Create a simple LinkedList'''
linked_list = LinkedList(Node(1)) # <-- Notice that we are passing a Node made up of an integer
linked_list.append(3) # <-- Notice that we are passing a numerical value as an argument in the append() function here 
linked_list.append(5)
linked_list.append(6)
linked_list.append(7)

''' Create another simple LinkedList'''
second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)
second_linked_list.append(8)
second_linked_list.append(9)

''' Create another simple LinkedList'''
third_linked_list = LinkedList(Node(10))
third_linked_list.append(13)
third_linked_list.append(15)

expected_list = [1,2,3,4,5,6,7,8,9,10,13,15] # <-- Python list


''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''
class NestedLinkedList(LinkedList):
    def flatten(self):
        # TODO: Implement this method to flatten the linked list in ascending sorted order.
        resultList = self.head
        print(resultList.value.to_list())
        listToCompare = resultList.next
        print(listToCompare.value.to_list())
        while listToCompare:
            resultList.value = merge(resultList.value,listToCompare.value)
            listToCompare = listToCompare.next
        return resultList.value


''' Create a NESTED LinkedList, where each node will be a simple LinkedList in itself'''

nested_linked_list = NestedLinkedList(Node(linked_list)) # <-- Notice that we are passing a Node made up of a simple LinkedList object
nested_linked_list.append(second_linked_list) # <-- Notice that we are passing a LinkedList object in the append() function here
nested_linked_list.append(third_linked_list) # <-- Notice that we are passing a LinkedList object in the append() function here
solution = nested_linked_list.flatten() # <-- returns A LinkedList object

assert solution.to_list() == expected_list, f"list contents: {solution.to_list()}"

#TODO

