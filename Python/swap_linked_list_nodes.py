class Node:
    """LinkedListNode class to be used for this problem"""
    def __init__(self, data):
        self.data = data
        self.next = None


def swap_nodes(head, left_index, right_index):
    
    # Get references to the nodes to the left of the nodes we want to swap 
    current = head

    onePrevious = None
    oneCurrent = None

    twoPrevious = None
    twoCurrent = None

    index = 0

    while current:

        if(index == left_index):
            oneCurrent = current
        elif(index == right_index):
            twoCurrent = current
            break

        if(oneCurrent is None): #On every loop where havent found the left index node
            onePrevious = current #Assign the current to previous. When we have found oneCurrent, this assignment will be correct
        
        twoPrevious = current #Now we continue, and when the elif statement is true and we break then this assignment will be correct

        index = index + 1
        current = current.next
   

    twoPrevious.next = oneCurrent #Point the node before the second swap node to the first swap node
    temp = oneCurrent.next #Save the reference from the node after the first swap node
    oneCurrent.next = twoCurrent.next #Point the node after the first swap to the node after the 2nd swap node
    twoCurrent.next = temp #
       
    
    if(onePrevious is None):
        newHead = twoCurrent
    else:
        newHead = head
        onePrevious.next = twoCurrent
      

    print_linked_list(newHead)

    # helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

arr = [3, 4, 5, 2, 6, 1, 9]
head = create_linked_list(arr)
    
swap_nodes(head,0,6)