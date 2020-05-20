/*

https://www.interviewcake.com/question/javascript/inflight-entertainment

Write a function that takes an integer flightLength (in minutes) and an array of integers movieLengths (in minutes) 
and returns a boolean indicating whether there are two numbers in movieLengths whose sum equals flightLength.

When building your function:

Assume your users will watch exactly two movies
Don't make your users watch the same movie twice
Optimize for runtime over memory

*/

function moviesForFlight(flightLength,movieLengths){
    var moviesSeen = new Set();
    var secondMovie; 
    for(var i = 0; i < movieLengths.length;i++){
        var firstMovieLength = movieLengths[i];
        secondMovie = flightLength - firstMovieLength;
        if(moviesSeen.has(secondMovie)){
            console.log(true)
            return true;
        }
        moviesSeen.add(firstMovieLength);
    }
    console.log(false);
    return false;
}

moviesForFlight(120,[60,60,90,120,30])

//Discard any movie > flightlength
//