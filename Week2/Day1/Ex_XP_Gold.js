// Exercise 1


let me = ["my","favorite","color","is","blue"];
let shmuel = me.join(" ");
console.log(shmuel);


// Exercise 2


var w1 = "mix";
var w2 = "pod";

w1array= w1.split("");
w2array= w2.split("");

var w3= w1array.slice(0,2);
w3.push (w2array[2]);
var w4= w2array.slice(0,2);
w4.push(w1array[2]);
console.log(w3);
console.log(w4);


console.log(w3.join("")+" "+w4.join(""))



// Exercise 3


// Addition
num1 = prompt("Please enter a number for addition","e.g 1")
num2 = prompt("Please enter a number for addition","e.g 1")

sum=parseInt(num1)+parseInt(num2)
alert(sum)

// // Subtraction 
num1 = prompt("Please enter a number for subtracion","e.g 1")
num2 = prompt("Please enter a number","e.g 1")

sum=parseInt(num1)-parseInt(num2)
alert(sum)


// // Multiplication
num1 = prompt("Please enter a number for mutiplication","e.g 1")
num2 = prompt("Please enter a number for multiplication","e.g 1")

sum=parseInt(num1)*parseInt(num2)
alert(sum)

// // Division
num1 = prompt("Please enter a number for Division","e.g 1")
num2 = prompt("Please enter a number for Division","e.g 1")

sum=parseInt(num1)/parseInt(num2)
alert(sum)

