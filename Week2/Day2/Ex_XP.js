// Excercise 1

// Create 2 variables, x and y. Each of them should have a different numeric value.
// Write an if/else statement that checks which number is bigger.

// let x = prompt("Enter x");
// let y = prompt("Enter y");

// let xint = parseInt(x);
// let yint = parseInt(y);

// if (xint <yint) {alert("x is the smaller number")}
// else if (xint > yint) {alert("x is bigger number")}
// else if (xint===yint) {alert("x and y are the same")};



// Exercise 2: Chihuahuasds

// Instructions

// Create a variable called newDog where it’s value is “Chihuahua”.
// Check and display how many letters are in newDog.
// Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just console.log twice).
// Check if the variable newDog is equal to “Chihuahua”
// if it does, display ‘I love Chihuahuas, it’s my favorite dog breed’
// else, console.log ‘I dont care, I prefer cats’

// let newDog="Chihuahua"
// let dog = prompt('Enter dog type')
// console.log(dog.length)
// console.log(dog.toUpperCase())
// console.log(dog.toLowerCase())
// if (dog==newDog) { alert("I love Chihuahuas, it’s my favorite dog breed")
//     }
// else  alert("I dont care, I prefer cats")





// Exercise 3: Even Or Odd

// Instructions

// Prompt the user for a number and save it to a variable.
// Check whether the variable is even or odd.
// If it is even, display: “x is an even number”. Where x is the actual number the user chose.
// If it is odd, display: “x is an odd number”. Where x is the actual number the user chose.

// let x = prompt ("Enter a number to cheak if its odd or even")
// if ( x % 2 == 0) {
// 	alert(x + " " +'is an Even Number');
// }else{
// 	alert(x + " " +'is an odd Number');
// }


// Exercise 4 : Switch Case

// Answers:
// 1. You encouter a monster
// 2.you arrive home and
// 3. You found a river 
// 4. You run into a troll


// Exercise 5: Group Chat

// Instructions

// let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]
// Using the array above, console.log the number of users in a group chat based on the following rules:
// If there is no users (the users array is empty), console.log “no one is online”.
// If there is 1 user, console.log “<name_user> is online”.
// If there are 2 users, console.log “<name_user1> and <name_user2> are online”.
// If there are more than 2 users, console.log the first two names in the users array and the number of additional users online.
// For example, if there are 5 users, it should display:


// let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]
// console.log(users.length)
// if (users.length ===0) 
// {console.log("no one is online");
// }
// else if (users.length===1) {console.log (users[0]+" "+ "is online");
// }
// else if (users.length===2) {console.log (users[0]+ " "+ users[1] +" "+ "is online");
// }
// else {console.log (users[0] +" " +users[1] +" "+ "and " + (users.length-2) +" more are online")}