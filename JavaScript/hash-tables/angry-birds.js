/*
Each round, players receive a score between 0 and 100, 
which you use to rank them from highest to lowest. 
So far you're using an algorithm that sorts in 0(nlogn) time,
but players are complaining that their rankings aren't updated fast enough. 
You need a faster sorting algorithm.

Write a function that takes:
- an array of unsortedScores
- the highestPossibleScore in the game
and returns a sorted array of scores in less than O(nlogn) time.

For example:

const unsortedScores = [37, 89, 41, 65, 91, 53];
const HIGHEST_POSSIBLE_SCORE = 100;

sortScores(unsortedScores, HIGHEST_POSSIBLE_SCORE);
returns [91, 89, 65, 53, 41, 37]
*/
const HIGHEST_POSSIBLE_SCORE = 100
function sort(array,highestPossibleScore){
    var temp; 
    var result = [];
    var map = new Map();
    for(let i = 0 ; i < array.length;i++){
        if(!map.has(array[i])){//if item doesn't exist
            map.set(array[i],1);//set item and count
        }else{
           var count = map.get(array[i]);
           count += 1
           map.set(array[i],count)
        }
    }
    for(var i = 0; i < HIGHEST_POSSIBLE_SCORE; i ++){
        if(map.has(i)){
            var count = map.get(i)
            for(var j = 0; i < count;j++){
                result.push(i)
            }
        }
    }
    return result;
}

function addToMap(num,count){

}
sort([3,0,0,0,1,1],HIGHEST_POSSIBLE_SCORE)
//sort([37, 89, 41, 65, 91, 53],highestPossibleScore)