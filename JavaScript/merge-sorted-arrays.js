//https://www.interviewcake.com/question/javascript/merge-sorted-arrays?course=fc1&section=array-and-string-manipulation

function mergeArray(array1, array2){
    var mergedArray = []; 
    var i = 0;
    var j = 0;

    while(mergedArray.length < array1.length + array2.length ){
        if(array1[i] < array2[j]){
            mergedArray.push(array1[i])
            i++    
        }else{
            mergedArray.push(array2[j])
            j++    
        }
    }

    return mergedArray;
}

const myArray = [2];
const alicesArray = [1];

console.log(mergeArray(myArray, alicesArray));
// logs [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]