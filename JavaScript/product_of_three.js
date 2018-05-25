/*Given an array of integers, find the highest product you can get from three of the integers.

The input arrayOfInts will always have at least three integers.*/

//[-4,-1,-2,3] if 1 positive return product of it and two smallest negatives

function splitArrayAndTestForZero(array){//split array into negative and positive array and test if 0 is in array
    var negativeArray = [],
    positiveArray = [],
    containsZero = false,
    result = [negativeArray,positiveArray,containsZero],
    firstValue;
    array.forEach(function(value){
        if(value > 0){
           positiveArray.push(value);
        }else if(value < 0){
            negativeArray.push(value);
        }else{
            containsZero = true;
        }
    })
    negativeArray.reverse();
    positiveArray.reverse();
    return result;
};

function prodOfThree(array){
    var splitArray = splitArrayAndTestForZero(array),
    negArray = splitArray[0],
    posArray = splitArray[1],
    containsZero = splitArray[2],
    product;
    if(posArray.length === 0 && containsZero){ //[-1,-2,-3,0] if negatives and no positives and 0, return 0
        product = 0;
    }else if(posArray.length === 2 && containsZero){//[2,1,0] if 2 positives and 0 return 0
       product = 0;
    }else if(posArray.length === 2 && !containsZero){//[-1,-2,3,4] if 2 positives and no 0 
        product = posArray[0] * posArray[1] * negArray[negArray.length-1];//todo this is wrong ^ 
    }
    else if(posArray.length === 0 && !containsZero){ //only negative numbers
        product = negArray[negArray.length-1] * negArray[negArray.length-2] * negArray[negArray.length-3];
    }else{//[-4,-1,-2,3] if 1 positive return product of it and two smallest negatives
        product = posArray[0] * negArray[0] * negArray[1];
    }
}



//[-1,-2,0,3,4]