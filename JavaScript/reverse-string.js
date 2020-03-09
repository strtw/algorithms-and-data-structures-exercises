// /https://www.interviewcake.com/question/javascript/reverse-string-in-place?course=fc1&section=array-and-string-manipulation

var reverse = ['c','a','o','t']

function reverseChars(array){ //This approach uses in place method. 
    var last;
    for(var i = 0 ; i < Math.floor(array.length/2); i++){ 
        last = array[array.length - 1 - i]
        array[array.length - 1 - i] = array[i]
        array[i] = last
    }
    
}

reverseChars(reverse)
console.log(reverse)

//==toac
//temp var to keep the second one to switch 
/* i with array.length - i 
how many times to switch? length/2 floor */