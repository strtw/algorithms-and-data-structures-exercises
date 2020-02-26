//https://www.interviewcake.com/question/javascript/reverse-words?course=fc1&section=array-and-string-manipulation



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
*/

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
    message.push(" ");
   
    for(let i = 0; i < message.length ; i++){
        if(message[i] === ' '){ //find a word boundary which is space or end of array
            endIndex = i - 1; //set the end index of the word to the character before the space
            reverseChars(message,startIndex,endIndex)  //reverse the characters 
            startIndex = i + 1 //set the next start index
        }
    }
    message.pop()
    console.log(message)
}

reverseWords(message1);
reverseWords(message2);