class Stack:
    
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0
        
    def push(self, data):
        if( self.num_elements == len(self.arr)):#Next push would exceed array length
            self._handle_stack_capacity() #Double the array size
        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1
        
    def _handle_stack_capacity(self):
        self.newArr = [0 for _ in range(self.num_elements * 2)]#New 2x long array
        for i, el in enumerate(self.arr):
            self.newArr[i] = el #copy arr values to new array
        self.arr = self.newArr #reassign arr

    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        if(self.num_elements == 0):
            return None
        elem = self.arr[self.next_index - 1]
        self.arr[self.next_index] = 0
        self.num_elements -= 1
        self.next_index -= 1
        return elem