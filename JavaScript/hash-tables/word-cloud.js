//https://www.interviewcake.com/question/javascript/word-cloud?course=fc1&section=hashing-and-hash-tables

//Input long string: "After beating the eggs, Dana read the next step. The next step after was to cook the eggs"
//Output: {after:2,beating:1, the:4, eggs:4,dana:1,read:1,next:2,step:2, was:1,to:1,cook:1,}
/*
function wordCloud(string){
   var inputString = string;
   var wordArr; 
   var set = new Set();
   var resultObj = {};
    inputString = inputString.toLowerCase();
    inputString = inputString.replace(/[^- 0-9a-zA-Z]/g, ''); //return alphanumeric words
    wordArr = inputString.split(" ");
    for(let i = 0; i < wordArr.length;i++){
        var currentWord = wordArr[i]
        if(set.has(currentWord)){
            resultObj[currentWord] = ++ resultObj[currentWord];
        }else{
            resultObj[currentWord] = 1
            set.add(currentWord);
        }
    }
    return resultObj;
}

console.log(wordCloud("After beating the eggs, Dana read the next-step. The next-step after was to cook the eggs"))

//module.exports = wordCloud;

*/

var numArr = [3,5,7,9,11]
var targetNum = 14;

//write functon that returns indeces of two 

function findTarget(array,targetNum){
    //let set = new Set();
    var result = false;
    for(let i = 0; i < array.length; i++){
        var currentNum = array[i];
        var numToFind = targetNum - currentNum
     for(let j = i; j < array.length; j++){
        var numToMatch = array[j];
        if(numToMatch === numToFind){
           // console.log(result,currentNum,numToMatch)
            return  result = [i,j];
     }
    }
}
}

findTarget(numArr,targetNum)



function findFirstAddends(numArray,sum){//didn't consult internet
    var set = new Set();
    for(let i=0;i<numArray.length;i++){
        var currentNum = numArray[i]
        var numToFind = sum - currentNum;
        if(!set.has(numToFind)){
            set.add(currentNum)
        }else{
            var firstMatch = i;
            for(let i = 0;i<numArray.length;i++){
                if(numArray[i] === numToFind){
                    console.log('First version', [i,firstMatch])
                    return [i,firstMatch]
                }
            }
        }
    }
    return false;
}




var numArr = [0,3,4,11,14,5,7,9]
var sum = 9;

function findFirstAddends1(numArray,sum){
    var map = new Map();
    for(let i=0;i<numArray.length;i++){
        var currentNum = numArray[i]
        var numToFind = sum - currentNum;
        if(map.has(numToFind)){
            console.log("Second version",[map.get(numToFind),i])
            return;
        }else{
            map.set(currentNum,i)
        }
    }
    return false;
}

findFirstAddends(numArr,sum)
findFirstAddends1(numArr,sum)