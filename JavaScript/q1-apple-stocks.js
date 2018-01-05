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
    var posResult = 0,
        negResult = Number.NEGATIVE_INFINITY, //set
        current = array[0],
        result;

    array.forEach(function(value, index){
        if(current < value && posResult < value - current){
            posResult = value - current;
        }else if(value < current && negResult < value - current ){
            negResult = value - current;
        }
        current = value;
    })

    if(negResult === Number.NEGATIVE_INFINITY){
        negResult = 0; // if buy and sell price is same
    }

    return  posResult > 0 ? posResult : negResult;
}

getMaxProfit(stockPricesYesterday);