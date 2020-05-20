

//this solution uses recursion 

 /*function mergeRanges(array){
    
    var result = [];
    var sortedArr = (function sortArr(array){ //Out-of-place approach
        var temp = 0;
        var result = [];
        array.forEach(function(item,index){
            if(item.startTime >= temp){
                result.splice(index,0,item)

            }else{
                result.splice(index-1,0,item)
            }
            temp = item.startTime;
        })
        return result;
    })(array)

    function merge(sortedArr){
        var unmerged; //has the array been merged if it can be
        var result = [];
        var endTime;
        for(let i = 0 ; i < sortedArr.length; i++){
        if(sortedArr[i+1] && sortedArr[i].endTime >= sortedArr[i+1].startTime){//if meetings overlap
            if(sortedArr[i].endTime > sortedArr[i+1].endTime){
                endTime = sortedArr[i].endTime //next meeting falls within current meeting, so set end time to current endtime
            }else{
                endTime = sortedArr[i+1].endTime // next meeting extends beyond current meeting, so set end time to next meeting
            }
            result.push({startTime:sortedArr[i].startTime, endTime:endTime}) //push merged result
            sortedArr.splice(i,1); //delete current meeting
            unmerged = true;
        }else{
            result.push(sortedArr[i])//no merge needed, so push to result
        }
    }
    return unmerged ? merge(result) : result //once all the merged have happened, the loop won't set the 'merged' flag to true, so the array will be returned
    }

   var result = merge(sortedArr); //run the recursive merge function on the array
   console.log(result);
    


}*/

/*mergeRanges(  [
/*{ startTime: 0,  endTime: 1 },
{ startTime: 3,  endTime: 5 },
{ startTime: 4,  endTime: 8 },
{ startTime: 10, endTime: 12 },
{ startTime: 9,  endTime: 10 }



{ startTime: 1, endTime: 10 },
{ startTime: 10, endTime: 11 },
{ startTime: 2, endTime: 6 },
{ startTime: 3, endTime: 5 },
{ startTime: 7, endTime: 9 },
]
)*/


// 2/20/2020 Solution. 
/*This solution takes up 0(1) space complexity because no additional space is allocated for the array. 
It's modified in place. However, in this implementation, the trade off is in time complexity because
the splice inside the loop is worst case O(n^2)
*/

/*function mergeRanges(array){ //Iterative approach
    array = array.sort(function compareNumbers(a, b) {//sort by startimes
        return a.startTime - b.startTime;
    })
    for(var i = 0; i < array.length; i++){
        if(array[i+1] && array[i+1].startTime > array[i].startTime  //if next meeting is within current meeting time block
            && array[i+1].endTime < array[i].endTime){  
            array.splice(i+1,1) //delete next meeting
            i-- //set index back one meeting so next loop with compare it with next meeting
        }else if(array[i+1] && array[i+1].startTime <= array[i].endTime){ // if next meeting overlaps with current meeting
            array[i].endTime = array[i+1].endTime; //update current meeting endtime to 'merge' meetings
            array.splice(i+1,1) //remove next meeting
            i--
        }
    }
    console.log(array)
    return array
}*/

function removeDuplicates(input){
    var result = [];
    var deduped = [];
    input = input.split(''); 
  for(let i = 0; i < input.length ; i++){
    result.push({index: i,character:input[i]}) //create an object that keep track of the index of a given character
  }
  result = result.sort(function compareLetters(a,b){ //sort the resulting array alphabetically
     return a.character.localeCompare(b.character)
  })

  deduped.push(result[0]) //add the first character in result to have something to compare against

  for( let i = 1; i < result.length ;i++){
      if(result[i].character.toLowerCase() === deduped[deduped.length -1].character.toLowerCase()){ //last duplicate character is same as current item in result array
        if(result[i].index < deduped[deduped.length-1].index ){// if it occurs first in the input string
            deduped[deduped.length -1] = result[i] //replace the duplicate character
        }  
      }else{
        deduped.push(result[i]) // current character isn't a duplicate so add it to the 
      }
  }
  result = []; //reset the result array

  deduped = deduped.sort(function compareIndexes(a,b){ //sort the deduped array by position of character
    return a.index- b.index
 })

 
 for(var i = 0; i < deduped.length; i++){
     result.push(deduped[i].character) //add the sorted characters to the result array
 }
 result = result.join('') //join into string
 return result;
}

removeDuplicates("AbraCadABraAlakAzam")
//removeDuplicates("Aa")
