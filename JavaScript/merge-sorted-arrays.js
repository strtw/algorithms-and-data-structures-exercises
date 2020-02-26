//https://www.interviewcake.com/question/javascript/merge-sorted-arrays?course=fc1&section=array-and-string-manipulation

function mergeArray(array1, array2){
    var mergedArray = [];
    var shorterArray = array1;
    var longerArray = array2;

    if(array1.length !== array2.length){
        shorterArray = array1.length < array2.length ? array1 : array2;
        longerArray = array1.length > array2.length ? array1 : array2;
    }

    for(let i = 0; i < shorterArray.length; i++){
        if(shorterArray[i] < longerArray[i]){
            mergedArray.push(shorterArray[i],longerArray[i])
        }else{
            mergedArray.push(longerArray[i],shorterArray[i])
        }
    }

    for(let i = shorterArray.length; i < longerArray.length; i++){
        mergedArray.push(longerArray[i]);
    }

    mergedArray.sort(function(a,b){
        return a - b;
    })

    return mergedArray;
}

const myArray = [3, 4, 6, 10, 11, 15];
const alicesArray = [1, 5, 8, 12, 14, 19, 20, 25, 30];

console.log(mergeArray(myArray, alicesArray));
// logs [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]