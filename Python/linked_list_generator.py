class Node:
      def __init__(self,value):
          self.value = value
          self.next = None


def create_linked_list(input_list):
    head = None
    if(len(input_list) >= 2):#Make sure the list is at least two items long (head and tail)
        head = Node(input_list[0])
        tail = Node(input_list[1])
        head.next = tail #link the tail to the head
        for value in input_list[2:]:#Start at third item in list
            tail.next = Node(value) #Create a new tail
    return head
        

linked = create_linked_list([1,2,3])

def iterateList(headNode):
    if(headNode):
      currentNode = headNode
      print(currentNode.value)
      while(currentNode.next is not None):
          print(currentNode.next.value)
          currentNode = currentNode.next
    else:
      return None

iterateList(linked)