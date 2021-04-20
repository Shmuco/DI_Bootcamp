
let fallingBottels=0


remainingBottels=(prompt("Enter a number"))
while (remainingBottels>fallingBottels){
var remainingBottels = remainingBottels -fallingBottels
console.log((remainingBottels+ " bottles of beer on the wall"));
console.log((remainingBottels+ " bottles of beer "));
fallingBottels++
if (fallingBottels>1) {
    console.log(("Take "+ fallingBottels +" down, pass them around"));
    console.log((remainingBottels+ " bottles of beer "));
}
else {console.log(("Take "+ fallingBottels +" down, pass it around"));
console.log((remainingBottels+ " bottles of beer "));
}

}


// if (remainingBottels> fallingBottels){
//     console.log((remainingBottels-fallingBottels)+ " bottles of beer on the wall");
//     console.log((remainingBottels-fallingBottels)+ " bottles of beer ");
//     console.log(("Take "+ fallingBottels +" down, pass it around"));}
// else if (remainingBottels)
