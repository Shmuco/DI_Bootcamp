// Exercise 1 : Keyless Car

// Instructions

// 1. Ask the user for their age, and save the value to a variable.
// 2. Create a function called checkDriverAge() that will
//    notify the user if they are permitted to drive. 
//    They must be at least 18 to drive.
//  -if the user is too young, alert “Sorry, 
//   you are too young to drive this car. Powering off”
// - if the user is old enough, alert “You are old 
//   enough to drive, Powering On. Enjoy the ride!”
// - if the user just turned 18, alert “Congratulations 
//   on your first year of driving. Enjoy the ride!”
// 3. Instead of using prompt to ask the user for their age, 
//    have the checkDriverAge() function accept an argument age.

// let usersage = (prompt("How old are you?"))
// function agecheck(age) {
//     if (age > 18) { 
//         alert("You are old enough to drive, Powering On. Enjoy the ride!")       
//     }
//     else if (age <18 ) {alert("Sorry,you are too young to drive this car. Powering off")
//     }
//     else {alert("Congratulations on your first year of driving. Enjoy the ride!")}   

// }

// agecheck(usersage)



// Exercise 2
// let wallet = []
// wallet.push(prompt("How many Quarters do you have?"))
// wallet.push(prompt("How many Dimes do you have?"))
// wallet.push(prompt("How many Nickles do you have?"))
// wallet.push(prompt("How many Pennies do you have?"))
// wallet.push(prompt("How much is the item?"))

// console.log(wallet)
// console.log((wallet[0]*0.25+wallet[1]*0.10+wallet[2]*0.05+wallet[3]*0.01))

// if ((wallet[0]*0.25+wallet[1]*0.10+wallet[2]*0.05+wallet[3]*0.01)> wallet[4]
// ) {alert("You have enough money")
// }
// else alert("You need more money")



// Exercise 3

// function mutiplies23 (number){
//     let i = 1
//     let result=0
//     let sum=0

// while (result <500) {   
//     console.log(result)
//     console.log(i)
    
//     result=i*23
//     sum=sum+result
//     i++
    
// }
// console.log("The final sum is "+ sum)
// } 
// mutiplies23(0)


// Exercise 4

// let amazonBasket = {
//   glasses: 1,
//   books: 2,
//   floss: 100,
// };
// function basketCheacker(input) {
//   if (input in amazonBasket) {
//     alert("We have " + amazonBasket[input] + " stock");
//   } 
//   else alert("That item is out of stcok");
// }

// basketCheacker(prompt("Enter an item to cheak"));


// Exercise 5 : Shopping List
// 1.Create an array called shoppingList with the following items: 
// “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.
// 2. Create a function called myBill() that takes no arguments.
// 3. The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// 4. The item must be in stock.
// 5. If the item is in stock find out the price in the prices object.
// 6. Call the myBill() function.
// Bonus: If the item is in stock, decrease the item’s stock by 1

// let stock = {
//   banana: 6,
//   apple: 0,
//   pear: 12,
//   orange: 32,
//   blueberry: 1,
// };

// let prices = {
//   banana: 4,
//   apple: 2,
//   pear: 1,
//   orange: 1.5,
//   blueberry: 10,
// };

// let cart = ["banana", "orange", "apple"];
// let total = 0;

// function myBill() {
//   for (let item of cart) {
//     if (item in stock && stock[item] > 0) {
//       total = total + prices[item];
//       stock[item] = stock[item] - 1;
//     } else continue;
//   }
//   console.log(stock);
//   console.log(total);
// }
// myBill(cart);


// Exercise 6 : Tips

// Instructions

// John created a simple tip calculator to help calculate how much to tip when he and his family go to restaurants.

// The calculator has the following rules:
// 1. Tip 20% when the bill is less than $50,
// 2. Tip 15% when the bill is between $50 and $200,
// 3. Tip 10% if the bill is more than $200.

// Ask John for the amount of the bill.
// Create the program explained above.
// In the end, John would like to know:
// Tip amount.
// Final bill (bill + tip).
// (NOTE: To calculate 20% of a value, simply multiply it with 20/100 = 0.2)


// let tip = 0
// function tipCalculator(amount) {
//     if (amount < 50){
//         tip = 0.2*amount
//     }
//     else if (amount<200)
//     tip = 0.15* amount

//     else tip= 0.1*amount
//     console.log(tip+amount)

//     alert ("The tip is: £"+tip+"\nThe Final bill is: £" + (tip+amount))

// }
// tipCalculator(parseInt(prompt("Please enter the amount")))



// Exercise 7 : Vacations Costs

// Instructions

// Let’s create functions that calculate your vacation’s costs:

// Define a function called hotel_cost().
// It should ask the user for the number of nights they would like to stay in the hotel.
// If the user doesn’t answer or if the answer is not a number, ask again.
// The hotel costs $140 per night. The function should return the total price of the hotel.
// Define a function called plane_ride_cost().
// It should ask the user for their destination.
// The function should return a different price depending on the location.
// “London”: 183$
// “Paris” : 220$
// All other destination : 300$
// If the user doesn’t answer or if the answer is not a string, ask again.
// Define a function called rental_car_cost().
// It should ask the user for the number of days they would like to rent the car.
// If the user doesn’t answer or if the answer is not a number, ask again.
// Calculate the cost to rent the car. The car costs $40 everyday.
// If the user rents a car for more than 10 days, they get a 5% discount.
// The function should return the total price of the car rental.
// Define a function called total_vacation_cost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z. 
// Hint: You have to call the functions hotel_cost(), plane_ride_cost() and rental_car_cost() inside the function total_vacation_cost.
// Call the function total_vacation_cost()
// Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the total_vacation_cost() function.


var hc =0;
function hotel_cost() {
    let nights = prompt('How many nights would you like to stay?')
    if (isNaN(nights) === true || (nights=="")){
    hotel_cost()}
    else { 
    hc = nights*140 
    console.log(hc)
    }  
}

var prc=0;
function plane_ride_cost() {
    destination= prompt("Please enter a detination")
    
    if (isNaN(destination) === true && destination != "null"){
        if (destination==="london"){
        prc= 183;
        }
        else if (destination==="paris"){
        prc= 220;
        }
        else prc = 300;
    }
    else plane_ride_cost()
    console.log(prc)
}

var rcc=0
function rental_car_cost () {
let days = prompt('How many days would you like the car?')
    if (isNaN(days) === true || (days=="")){
    rental_car_cost()}
    else { 
        if (days<=10){
            rcc = days*40;
        }
        else rcc =0.95*(days*40)
    console.log(rcc)
    
}  
}
function total_vacation_cost() {
    hotel_cost()
    plane_ride_cost()
    rental_car_cost()

    alert("The hotel cost: $"+ hc+"\nThe Plane tickets cost: $"+ prc+"\nThe Car rental cost: $"+ rcc+"\nTotal: $"+(hc+prc+rcc))
}

total_vacation_cost()