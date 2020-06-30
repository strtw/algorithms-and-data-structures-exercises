def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.
    
    Args:
       input(str): input to be checked if it is palindrome
    """
    
    result = False # Set the initial result to false
    
    if len(input) > 0 and input[:1] == input[-1]: # If the first and last character of the string are the same it passes to the next check
        result = True #Set the result to true
        is_palindrome(input[1:len(input)-1])#Run the check on the next set of characters
    elif(input == ""):
        result = True #Set the result to true for the last check
  
    return result

print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")