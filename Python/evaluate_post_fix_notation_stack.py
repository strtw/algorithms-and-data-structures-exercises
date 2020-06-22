

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack:
    
    def __init__(self):
        self.head = None
        self.num_elements = 0
        
    def push(self, value):
        new_node = Node(value)
        # if stack is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head # place the new node at the head (top) of the linked list
            self.head = new_node

        self.num_elements += 1
        
    def pop(self):
        if self.is_empty():
            return
        
        value = self.head.value # copy data to a local variable
        self.head = self.head.next # move head pointer to point to next node (top is removed by doing so)
        self.num_elements -= 1
        return value
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0




def evaluate_post_fix(input_list):
    """
    Evaluate the Polish postfix notation expression to find the answer

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
    """
    stack = Stack()
    for element in input_list:
        if(element == '*'): #2. Check the operator, to have a valid expression there needs to be 2 operands on the stack now
            second = stack.pop() #3. Last in first out, so the first one out is the second one in
            first = stack.pop() #4. Second one out is the first element we put on the stack
            output = first * second #5. Get the result of the calculation
            stack.push(output) #6. Put it on the top of the stack. On the next loop, this will be the expressions total to this point and will be the second item, the first will be the next number in the list
        elif(element == '/'):
            second = stack.pop()
            first = stack.pop()
            output = int(first / second)
            stack.push(output)
        elif(element == '+'):
            second = stack.pop()
            first = stack.pop()
            output = first + second
            stack.push(output)
        elif(element == '-'):
            second = stack.pop()
            first = stack.pop()
            output = first - second
            stack.push(output)
        else: #1. If the element is not an operator put it on the stack. 
            stack.push(int(element))
    return stack.pop()



def test_function(test_case):
    output = evaluate_post_fix(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")

test_case_1 = [["3", "1", "+", "4", "*"], 16] # (3 + 1) * 4

test_function(test_case_1)