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

    reverseChars(message, 0, message.length-1) // reverse all the characters
    var index = [0]; //set a new array to hold the indexes of first and last work, and space delimeters
    for(let i = 0; i < message.length ; i++){
        if(message[i] === ' '){
            index.push(i) //add the locations of spaces to the index
        }
    }
    index.push(message.length) //add the length of the array to the index
    var startIndex = 0 //because this is the beginning of the first word
    var endIndex = index[1] - 1 //the character before the first space is the last character of the first word
    for(let i = 0; i < index.length; i++){
        reverseChars(message,startIndex,endIndex) 
        startIndex = index[i + 1] + 1 //the position of the next space, plus one character is the beginning of the next word
        endIndex = index[i + 2] - 1 //the position of the next space, minus one is the end of the next word
    }
    console.log(message)
}

reverseWords(message1);
reverseWords(message2);