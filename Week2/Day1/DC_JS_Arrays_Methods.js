// Exercise 1:

// Remove Banana from the array.
var fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.shift();
console.log(fruits);

// Sort the array in alphabetical order
fruits.sort();
console.log(fruits)

// Add “Kiwi” to the end of the array.
fruits.push("Kiwi");
console.log(fruits);

// Remove “Apples” from the array. Don’t use the same method as in part 1.
fruits.splice(0,1);
console.log(fruits);

// Sort the array in reverse order. 
// (Not alphabetical, but reverse the current Array i.e. [‘a’, ‘c’, ‘b’] becomes [‘b’, ‘c’, ‘a’])
fruits.reverse();
console.log(fruits);




// Exercise 2:
let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
let fruits = moreFruits [1];
console.log(fruits);
let lessfruits = fruits [1];
console.log(lessfruits);
let oranges = lessfruits [0];
console.log(oranges)

