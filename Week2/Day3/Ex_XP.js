
// Exercise 1 : Your Favorite Colors

// Instructions

// Create an array called colors where the value is a list of your favorite colors.
// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus


// let colors = ["Red","Yellow","Green", "Blue"]
// for (i in colors) {console.log("My #"+(parseInt(i)+1)+" fav" +" colour is "+ colors[i])}



// let colors = [["Red", "st"],["Yellow","nd"],["Green","rd"],["Blue","th"]]
// for (i in colors) {console.log("My " +(parseInt(i)+1) + colors[i][1] +" favorite colour is "+ colors[i][0])};



// Exercise 2 : List Of People

// Instructions










// 1. let people = ["Greg", "Mary", "Devon", "James"]
// let people = ["Greg", "Mary", "Devon", "James"];
// 2. Write code to remove “Greg” from the people array.
// people.shift();
// console.log(people)
// 3. Write code to replace “James” to “Jason”.
// 3. Write code to replace “James” to “Jason”.
// for (x in people){
    // if (people[x]=== "James") {
        // people.splice(x,1,"Jason");
    // }}

//     else continue
// console.log(people);

// 4. Write code to add your name to the end of the people array.
// people.push(prompt("Enter your name:"))
// console.log(people)

// 5. Using a loop, iterate through the people array and console.log each person.
// for (name in people){
//     console.log(people[name])
// }

// 6. Using a loop, iterate through the people array and after you console.log “Jason” exit the loop
// for (name in people){

//     if (people[name]=== "Jason"){
//         console.log(people[name]);
//         break;
//     }
    
    // else console.log(people[name])
// }
// 7. Write code to make a copy of the people array using slice. 
// The copy should NOT include “Mary” or your name.

// console.log(people)

// let people2 =[]
// for (name in people){
//     if (people[name]!== "Shmuel" && people[name]!= "Mary")
//     people2.push(people[name])
// }
// console.log(people2)


// let people2 =[]
// for (name in people){
//     if (people[name]!== "Shmuel" && people[name]!= "Mary")
//     people.slice(people),(people.slice(people)+1)
// }
// console.log(people2)

// 8. Write code that console.logs Mary’s index. take a look at indexOf on google.

// console.log(people.indexOf('Mary'))

// 9. Write code that gives the indexOf “Foo” (this should return -1). Why does it return -1
// console.log(people.indexOf('Foo'))
//Because there is no item in the array 'Foo'


// 10. Create a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?

// var last = people[people.length - 1];
// // console.log(people[-1])----why doesnt this work??
// console.log(last)



// Exercise 3 : Repeat The Question

// Instructions

// Prompt the user for a number, while the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?
// Hint : Check the data type you receive from the prompt (ie. typeof method)

while (prompt("Enter a number")<10) {
    continue
}
