/**
 * Created by stu on 11/8/17.
 */
/*
 Suppose we could access yesterday's stock prices as an array, where:

 The indices are the time in minutes past trade opening time,
 which was 9:30am local time.
 The values are the price in dollars of Apple stock at that time.
 So if the stock cost $500 at 10:30am, stockPricesYesterday[60] = 500.

 Write an efficient function that takes stockPricesYesterday and
 returns the best profit I could have made from 1 purchase
 and 1 sale of 1 Apple stock yesterday.
 */


//var stockPricesYesterday = [10, 7, 5, 8, 11, 9];
var stockPricesYesterday = [10, 8, 1, 5];


function getMaxProfit(array){
    var posResult = 0, negResult;
    for(let i = 0; i < array.length-1;i++){
        for(let j = i + 1; j < array.length ; j++ ){
            if(array[j] - array[i] > 0 && array[j] - array[i] > posResult){
                posResult = array[j] - array[i];
            };
            if(negResult === undefined && array[j] < array[i]){
                negResult = array[j] - array[i];
            }else if(array[j] < array[i] && Math.abs(array[j] - array[i]) < Math.abs(negResult)){
                negResult = array[j] - array[i];
            };
        }
    }

    console.log(posResult > 0 ? posResult : negResult);
    return posResult > 0 ? posResult : negResult;
}

getMaxProfit(stockPricesYesterday);
// returns 6 (buying for $5 and selling for $11)