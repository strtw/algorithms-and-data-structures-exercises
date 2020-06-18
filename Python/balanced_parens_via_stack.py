class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
       
    General idea: by popping off a '(' every time we encounter a ')'
    at the end of the equation we will either have popped off all the '('
    which indicates that we had a matching ')' or we will have either a length > 1 
    which means there was a surplus of '(' or if we pop and there's nothing to pop 
    that means we have at least one additional ')' so we return false
    """
    stack = Stack()
    
    for char in equation:
        if( char == '('): 
            stack.push(char)
        elif(char == ')'):
            if stack.pop() == None:
                return False
    return stack.size() == 0

print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")