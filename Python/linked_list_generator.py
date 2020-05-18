class Node:
      def __init__(self,value):
          self.value = value
          self.next = None


def create_linked_list(input_list):
    head = None
    for value in input_list:
        if head is None:
            head = Node(value) 
            tail = head
        else:
        # Move to the tail (the last node)
            tail.next = Node(value)
            tail = tail.next
    return head
        

linked = create_linked_list('string')

def iterateList(headNode):
      currentNode = headNode
      print(currentNode.value)
      while(currentNode.next is not None):
          print(currentNode.next.value)
          currentNode = currentNode.next

iterateList(linked)