# You are given a non-negative number in the form of list elements. 
# For example, the number 123 would be provided as arr = [1, 2, 3]. 
# Add one to the number and return the output in the form of a new list.

def add_one(arr): #0(n)
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """    
    for i in range( len(arr) - 1, -1, -1) : #Iterate through list backwards
        if(arr[i] == 9):#If current number is 9
            arr[i] = 0 #'Add one' by setting it to 0
            if(i == 0): #If the current index is the left most digit
                arr = [1] + arr #Prepend 1 to the number as the carry over
                break #Break out of the loop
        else:
            arr[i] = arr[i] + 1 #If the number is less than nine, just add one to it. 
            #If we are in a position to the left of the one's position, then this addition is a carry over
            break
    
    print(arr)
    return arr

add_one([1,0,9])