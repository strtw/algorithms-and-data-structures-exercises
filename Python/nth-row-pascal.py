def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    if(n == 1):
        return 1
    currentRow = [1] # Set the current row with an initial start of 1
    for i in range(1, n + 1): #0th row is top of triangle, outerloop keeps track of rows
        previousRow = currentRow #Give a reference to the previous row for the next loop iteration
        currentRow = [1] #Start building the current row
        for j in range(1,i):#Inner loop adds cells
           currentRow.append(previousRow[j] + previousRow[j-1])#Append the sum of the previous row cells at j and j-1
        currentRow.append(1)# Append at i position
    return currentRow #Return the current row  at n

print(nth_row_pascal(7))