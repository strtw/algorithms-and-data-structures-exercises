//https://www.interviewcake.com/question/javascript/reverse-words?course=fc1&section=array-and-string-manipulation

/*

const message1 = [ 'c', 'a', 'k', 'e', ' ',
                'p', 'o', 'u', 'n', 'd', ' ',
                's', 't', 'e', 'a', 'l' ];


const message2 = ['c','a','t',' ','l','i','k','e','s',' ','f','i','s','h']

//console.log(message.join(''));
// Prints: 'steal pound cake'

/*
function reverseChars(array){ //This approach uses in place method with for loop
    var last;
    for(var i = 0 ; i < Math.floor(array.length/2); i++){ //number of swaps is half the word count, i++ steps right
        last = array[array.length - 1 - i] //step left 
        array[array.length - 1 - i] = array[i]
        array[i] = last
    }
    
}


function reverseChars(array,startIndex,endIndex){ //This approach uses in place method with while loop
    var temp;
    while(startIndex < endIndex){//when start === end, the middle of the array has been reached
        temp = array[endIndex]
        array[endIndex] = array[startIndex];
        array[startIndex] = temp;
        startIndex++;
        endIndex--;
    }
    
}




function reverseWords(message){

    var startIndex = 0 //because this is the beginning of the first word
    var endIndex;

    reverseChars(message, 0, message.length-1) // reverse all the characters
   
    for(let i = 0; i <= message.length ; i++){
        if(message[i] === ' ' || i === message.length){ //find a word boundary which is space or end of array
            endIndex = i - 1; //set the end index of the word to the character before the space
            reverseChars(message,startIndex,endIndex)  //reverse the characters 
            startIndex = i + 1 //set the next start index
        }
    }
    console.log(message)
}

reverseWords(message1);
reverseWords(message2);

*/
/*
function longestEvenWord(sentence) {
    sentence = sentence + " ";
    let word = '';
    let wordStart = 0;
    let wordEnd;
    let longestWord = '';
    for(let i = 0;i<sentence.length;i++){
        wordEnd = i;
        if(sentence[i] === " " ){
            word = sentence.substring(wordStart,wordEnd);
            if(word.length % 2 === 0 && word.length > longestWord.length){
                longestWord = word;
            }
            wordStart = i+1;
        }
    }
   
    return longestWord;
}

longestEvenWord("I am a very happy soul")*/

/*Caesars cipher
function applyCipher(string,shift){
    var result = "";
    for(let i = 0;i<string.length;i++){
      var currentLetter = string[i];
      var currentCharCode = currentLetter.charCodeAt();
      var newCharCode;
      if(currentLetter !== " "){
       newCharCode = currentCharCode + shift
       let newChar = String.fromCharCode(newCharCode)
       result += newChar
      }
    }
    return result; 
  }

  applyCipher("ABC",2)*/

  /*A palindrome is a word, number, phrase, or another sequence of characters which
reads the same backward as forward, such as madam, racecar, or the number

What is the sum of all numeric palindromes that are less than 10,000?
*/
/*
function isPallindrome(string){
    let stringArray = string.split('');
    let endIndex = string.length - 1;
    let startIndex = 0
    while(startIndex < endIndex){
        if(stringArray[startIndex] !== stringArray[endIndex] ){
            return false;
        }
        startIndex++;
        endIndex--;
    }
    return true;
}


function returnPallindromeSumLessThan(num){
    var numString;
    var pallindromes = [];
    var result;
    for(let currentNum = 0; currentNum < num; currentNum++){
        numString = currentNum.toString();
        if(isPallindrome(numString)){
            pallindromes.push(Number(numString))
        }
    }
    result = pallindromes.reduce(( accumulator, currentValue ) => accumulator + currentValue, 0);
    return result;
}

returnPallindromeSumLessThan(10000);
*/

/*
Legionaries
In the range 1 - 13 (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13) the digit 1
occurs 6 times.

In the range, 1 - 2,660 (half the number of Romans in a legion), expressed in
Roman numerals, how many times does the numeral “X” occur?*/


function convertIntegerToRoman(int){
    var result = ''
    var romanNumerals = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"];
    values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    for(let i = 0; i < values.length; i++){
        while(values[i] <= int){
            result += romanNumerals[i];
            int = int - values[i];
        }
    }
    return result;
}

convertIntegerToRoman(3001);





/*Given the following quote by Alan Perlis

Dealing with failure is easy: Work hard to improve. Success is also easy to
handle: You’ve solved the wrong problem. Work hard to improve.

Considering only the alphabetical characters, consonants having the value of
their ASCII codes, and vowels having the inverse value of their ASCII codes,
what is the sum of the sentence?

Example:
Taking the word “iffy”, the ASCII code of “i” is 105, it’s inverse is -105.
The ASCII value of ‘f’ is 102. The ASCII y of “y” is 121. The sum of “iffy” =
220*/


