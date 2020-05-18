class Node:
      def __init__(self,value):
          self.value = value
          self.next = None


def create_linked_list(input_list):
    head = None
    tail = None
    for value in input_list:
        if head is None:
            head = Node(value) 
        elif tail is None:
            tail = Node(value)
            head.next = tail
        else:
        # Move to the tail (the last node)
            tail.next = Node(value)
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