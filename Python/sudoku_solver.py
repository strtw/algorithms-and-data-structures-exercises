
def check_sudoku(square):
    for row in square:#look at each row
        for i in range(len(square)):#number of checks equal to number of cells
                if not i+1 in row: #each check looks to see if 1...n where n is length of row exists
                    return False #if one of the expected number doesn't exist
                
    for i in range(len(square)):#Number of columns to build and test
        currentColumn=[] 
        for row in square:#look at each row
            columnCell = row[i] #grab the cell in column i
            currentColumn.append(columnCell)# append column cell to column
        #Column is built now
        for i in range(len(currentColumn)):#look at each column cell
            if not i+1 in currentColumn:# if expected number isn't in column
               return False
           
    return True




correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
incorrect6 = [[1, 2, 3],
                [1, 2, 3],
                [1, 2, 3]]
               
# Define a function check_sudoku() here:


print(check_sudoku(incorrect6))
#>>> False    
    
#print(check_sudoku(incorrect))
#>>> False

print(check_sudoku(correct))
#>>> True

print(check_sudoku(incorrect2))
#>>> False

print(check_sudoku(incorrect3))
#>>> False

print(check_sudoku(incorrect4))
#>>> False

print(check_sudoku(incorrect5))
#>>> False

"""
The input 
"[[1, 2, 3],
 [1, 2, 3],
 [1, 2, 3]]"
should return: False


The input 
"[[1]]"
should return: True


The input 
"[[1, 2],
 [2, 1]]"
should return: True


The input 
"[[1, 2, 4],
 [2, 4, 1],
 [4, 1, 2]]"
should return: False


The input 
"[[2, 2, 2],
 [2, 2, 2],
 [2, 2, 2]]"
should return: False


The input 
"[[1, 2, 3, 4],
 [2, 4, 1, 3],
 [3, 1, 4, 2],
 [4, 3, 2, 1]]"
should return: True


The input 
"[[0, 1, 2],
 [2, 0, 1],
 [1, 2, 0]]"
should return: False
"""
