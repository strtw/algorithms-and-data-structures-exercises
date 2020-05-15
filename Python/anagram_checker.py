def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other
    don't take into account white space
    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
 
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    if len(str1) != len(str2):
        return False

    str1 = set(str1)
    str2 = set(str2)#
    for char in str2: 
        if(char not in str1):
            return False
    return True

print(anagram_checker("cat","tac"))#True
print(anagram_checker("cato","tac"))#False
print(anagram_checker('water','waiter'))#False
print(anagram_checker('Dormitory','Dirty room'))#True