# LinkedList Node class for your reference
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
You are given the head of a linked list and two integers, i and j.
You have to retain the first i nodes and then delete the next j nodes. 
Continue doing so until the end of the linked list.
'''

def skip_i_delete_j(head, i, j):

    current = head
    previous = None

    while current:

        #Retain i nodes
        for node in range(i - 1):
            if current is None:
                return head
            current = current.next # advanced e.g. 'skip' the current node
        previous = current #Keep a reference to the last retained node in this iteration of the while loop
        current = current.next #Now, we advance to the node after the reference node, the first node to be skipped

        #Skip j nodes
        for node in range(j): #Starting with the newly assigned current node, we advance j nodes
            if current is None:
                break
           # nextNode = current.next #
            #current = nextNode
            current = current.next
        
        previous.next = current
    print_linked_list(head)
    return head

       







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
        print(head.data, end=' ')
        head = head.next
    print()


def test_function(test_case):
    head = test_case[0]
    i = test_case[1]
    j = test_case[2]
    solution = test_case[3]
        
    temp = skip_i_delete_j(head, i, j)
    index = 0
    try:
        while temp is not None:
            if temp.data != solution[index]:
                print("Fail")
                return
            index += 1
            temp = temp.next
        print("Pass")
    except Exception as e:
        print("Fail")


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 2
head = create_linked_list(arr)
solution = [1, 2, 5, 6, 9, 10]
test_case = [head, i, j, solution]
test_function(test_case)