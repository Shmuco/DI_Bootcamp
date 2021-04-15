// Exercise 1

// 1. Create a structured html file linked to a js file
// 2. Write a JS function that takes a parameter: myAge
// 3. Console.log the age of my mum and my dad (my mum is twice my age, and my dad is 1.2 the age of my mum)
// 4. Call the function


//method 1
// function ageCalc(yourage) {
//     console.log("Your mum is " + (yourage*2) + " your dad is " + (yourage*2*1.2).toFixed())
// }

// ageCalc(prompt("How old are you?")) 

//method2
// function ageCalc(yourage) {
//     let mumage = yourage*2
//     console.log("Your mum is " + (mumage) + " your dad is " + (mumage*1.2).toFixed())
// }

// ageCalc(prompt("How old are you?")) 


// Exercise 2

// 1. Create a structured html file linked to a js file
// 2. Write a JS function that takes a parameter: myAge
// 3. Return the age of my mum (my mum is twice my age)
// 4. Call the function
// 5. Console.log the age of my mum


// ageCalc(prompt("How old are you?"))
function ageCalc(yourage) {
    let mumage = yourage*2
    return("Your mum is " + (mumage) + " your dad is " + (mumage*1.2).toFixed())
}



let finalage = ageCalc(prompt("How old are you?"))
console.log(finalage)


const profile = (username, password) => "user: " + username + " Password: " + password
console.log(profile("User","Password"))