/*Write an efficient function that checks whether any permutation ↴ of an input string is a palindrome. ↴

You can assume the input string only contains lowercase letters.

Examples:

"civic" should return true
"ivicc" should return true
"civil" should return false
"livci" should return false
*/

//What is a palindrome? A string where comparing the two ends and moving in returns the same character. 
//This means that the string has an equal number of character pairs, with the exception of 1 character.  

/*
function palindrome(string){ implementation using set and object
    var set = new Set();
    var counts = {};
    var oddCharCount = 0;
   
    for(var i = 0; i < string.length; i++){
        if(!set.has(string[i])){ //if set doesn't have current character
            set.add(string[i]);//add current character to set
            counts[string[i]] = 1; //add the character to counts object
        }else{
            counts[string[i]] ++; //if set has the character, increment the count for the character
          }
        }

    for(var char in counts){
        if(counts[char] % 2 !== 0){//if there's an odd number of the character
            oddCharCount++ //add to the total count of characters with odd count
            if(oddCharCount > 1){// if there is more than 1 character with odd count it means the string doesnt pair off per character type
                console.log(false)
                return false;
            }
        }
    }
    console.log(true);
        return true;

    }
*/


   /* function palindrome(string){ //implementation using object. Could counts of characters to store even/odd but storing booleans prevents integer overflow
        var set = new Set();
        var counts = {};
        var oddCharCount = 0;
       
        for(var i = 0; i < string.length; i++){
            if(!counts[string[i]]){ //if set doesn't have current character
                counts[string[i]] = false; //false reprennts odd count
            }else{
                if(counts[string[i]] === true){//true represents even count
                    counts[string[i]] = false;
                }else{
                    counts[string[i]] = true;
                }
            }
        }
    
        for(var char in counts){
            if(!counts[char]){//if there's an odd number of the character
                oddCharCount++ //add to the total count of characters with odd count
                if(oddCharCount > 1){// if there is more than 1 character with odd count it means the string doesnt pair off per character type
                    console.log(false)
                    return false;
                }
            }
        }
        console.log(true);
            return true;
    
        }
       */
   

      /*function palindrome(string){ //implementation using set
        var set = new Set();
        
        for(var i = 0; i < string.length; i++){
            if(!set.has(string[i])){ //if set doesn't have current character
                set.add(string[i]); //add the character to the set representing an ODD count
            }else{
                set.delete(string[i]); //remove the character, representing an EVEN count
            }
        }

        if(set.size > 1){//if there is more than 1 characters with an odd count
            console.log(false)
            return false;//then the string can't pair off into a palindrome
        }else{
            console.log(true)
            return true;
        }
        
    }*/

    function palindrome(string){ //implementation using set, cleaned up for readability 
        var set = new Set();
        
        for(let char of string){
            if(set.has(char)){ //if set doesn't have current character
                set.delete(char); //add the character to the set representing an ODD count
            }else{
                set.add(char); //remove the character, representing an EVEN count
            }
        }
        console.log(set.size <= 1);
        return set.size <= 1;
    } 
       



palindrome("civic")//true
palindrome("ivicc")//true
palindrome("civil");//false
palindrome("livci");//false
palindrome("ccci");//false
palindrome("dci");//false
palindrome("oooo");//true