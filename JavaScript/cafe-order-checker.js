/*www.interviewcake.com/question/javascript/cafe-order-checker

Given all three arrays, write a function to check that my service is first-come, first-served. 
All food should come out in the same order customers requested it.

Take Out Orders: [1, 3, 5]
 Dine In Orders: [2, 4, 6]
  Served Orders: [1, 2, 3, 5, 4, 6]

Take Out Orders: [0, 1]
 Dine In Orders: [2, 4, 6]
  Served Orders: [2, 0, 1, 4, 6]

Take Out Orders: [0, 1]
 Dine In Orders: [2, 4, 6]
  Served Orders: [2, 4, 0, 6, 1]

Take Out Orders: [ ]
 Dine In Orders: [2, 4, 6]
  Served Orders: [2, 6, 4] //false

  This is first come first serve. Orders from one register may be served in front of orders from the
  other register, but orders from each register must still be served in the order they were taken. 
  This is to avoid a dine-in customers being served out of place. 
*/

function firstServe(dineIn,takeOut,served){
    //compare n item in served array with "first" item in other arrays
    var dineInIndex = 0;
    var takeOutIndex = 0;

    for(var i = 0; i < served.length; i++){
        if(dineIn[dineInIndex] && served[i] === dineIn[dineInIndex]){
            dineInIndex++
        }else if(takeOut[takeOutIndex] && served[i] === takeOut[takeOutIndex]){
            takeOutIndex++
        }else{
            console.log(false);
            return false;
        }
    }
    return true;
    //if first item in array matches either other array first item, proceed
    //advance whichever array matched to the next index position effective making it the 
        //'first' item in the next pass of the loop
    //if the index position of an array exceeds its length, ignore that array
    //and just do a comparison of the remaining index position for served and other array
}

firstServe([],[2,4,6],[2,6,4]) //false
firstServe([1,3,5],[2,4,6],[1,2,3,5,4,6]) //true
firstServe([0,1],[2,4,6],[2,0,1,4,6]) //true