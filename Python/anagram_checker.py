def anagram_checker(str1, str2):#0(n) worse case time complexity
    """
    Check if the input strings are anagrams of each other
    don't take into account white space
    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    str1 = str1.replace(" ", "").lower()#0(n)
    str2 = str2.replace(" ", "").lower()#0(n)

    if(countCharDict(str1) == countCharDict(str2)):#0(n)
        return True
    else:
        return False

def countCharDict(string):#0(n)
    stringDict = {}
    for char in string:#0(n)
        if( stringDict.get(char)):
            stringDict[char] = stringDict[char] + 1
        else:
            stringDict[char] = 1
    return stringDict



print(anagram_checker("cat","tac"))#True
print(anagram_checker("cato","tac"))#False
print(anagram_checker('water','waiter'))#False
print(anagram_checker('Dormitory','Dirty room'))#True
print(anagram_checker('A gentleman','Elegant men'))#False