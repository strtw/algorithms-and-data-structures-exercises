def reverseCharacters(string):#0(n), 0(n)
    result = ''
    for i in range(len(string)):
        result = result + string[(len(string)-1) - i]
    return  result

#print("Pass" if ("tac" == reverseCharacters("cat")) else "Fail")

def word_flipper(our_string):#0(n^2), 0(n)

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """
    result = ""
    startIndex = 0
    for i in range(len(our_string)):#0(n)
        if(our_string[i] == " "):
            word = our_string[startIndex:i]
            word = reverseCharacters(word) #0(n)
            result = result + word + " "
            startIndex = startIndex + len(word) + 1
        elif(i == len(our_string) - 1 ):
            word = our_string[startIndex:i+1]
            word = reverseCharacters(word) #0(n)
            result = result + word
            startIndex = startIndex + len(word)  
    return result


print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")

