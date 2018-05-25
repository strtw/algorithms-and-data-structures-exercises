/**
 * Created by stu on 1/5/18.
 */
/* You have an array of integers, and for each index you want to find the
product of every integer except the integer at that index.

Write a function getProductsOfAllIntsExceptAtIndex() that takes an array of
integers and returns an array of the products.

For example, given:

[1, 7, 3, 4]

your function would return:

[84, 12, 28, 21]

by calculating:

    [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Division is not allowed in solution
    */

//

//For each index in the array (outer loop) set that index to 1
// and multiply it by every index in the array (inner loop)
// when inner loop reaches the original value index of outer loop index,
// set inner value to 1 so product doesn't increase. A count is maintained for
// last step to ensure that the inner index is set to 1 only once for any
// given outer value
/*function getProductsOfAllIntsExceptAtIndex(array){
    var result = [],
        excludedValue,
        count,
        product;
    array.forEach(function(excludedValue){
        count = 0;
        originalValue = excludedValue;//keep track of outer value
        excludedValue = 1;//set to one so product doesn't increase when multipled by other indices
        array.forEach(function(includedValue){
            if(includedValue === originalValue && count <1 ){//the first time the loop encounters the value to be excluded
                includedValue = 1; //set to one so product doesn't increase when multipled
                count++ ;
            }
            excludedValue *= includedValue;//multiply
        });
        result.push(excludedValue);

    });
    return result;
}*/

//  [84, 12, 28, 21]

window.onload = function(){
    getProductsOfAllIntsExceptAtIndex([1,7,3,4]);
}

function getProductsOfAllIntsExceptAtIndex(array){
    var before = getProductsBeforeIndex(array);
    var after = getProductsAfterIndex(array);
    var result = [];
    var product = 1;//intitial product
    array.forEach(function(value,index,array){
        var beforeIndex = isNaN(before[index-1])? 1 : before[index-1];//set to 1 if referenced index is < 0
        var afterIndex = isNaN(after[index+1])? 1 : after[index+1];//set to 1 if referenced index is > than index length
        product = beforeIndex * afterIndex;
        result.push(product);
    })
    return result;
}

function getProductsBeforeIndex(array){
    var product = 1;
    var result = [];
    array.forEach(function(value){
        product *= value;
        result.push(product);
    })
    return result;
}

function getProductsAfterIndex(array){
    var product = 1;
    var result = [];
    for(let i = array.length-1; i >=0; i--){
        product *= array[i];
        result.unshift(product);
    }
    return result;
}


//5 * 2 * 8 * 9   
//10 * 2 * 8 * 9
//10 * 5 * 8 * 9
//10 * 5 * 2 * 9
//10 * 5 * 2 * 8



/*
0,7,3,4 = 84,0,0,0

 2*5*6, 1*5*6,1*2*6,1*2*5





*/



