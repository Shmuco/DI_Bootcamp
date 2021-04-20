// Exercise 1 : Change The Navbar

// 1. In the <div> above, change the value of the id attribute from navBar to socialNetworkNavigation, 
// using the setAttribute method.

// document.getElementById('navbar').id='social';

// 2. We are going to add a new <li> to the <ul>.
//    First, create a new <li> tag (use the createElement method).
//    Create a new text node with “Logout” as its specified text.
//    Append the text node to the newly created list node (li).
//    Finally, append this updated list node to the unordered list above, using the appendChild method.

// let logout = document.createElement("li")
// li.innerText = "Log Out"
// document.querySelector("ul").appendChild(logout)

// 3. Bonus
// Use the firstElementChild and the lastElementChild properties to retrieve the first and last li elements
//  from their parent element (ul). Display the text of each link. (Hint: use the textContent property).

// document.querySelector("ul").firstElementChild.textContent
// document.querySelector("ul").lastElementChild.textContent


// Exercise 2 : Users

// 1. In the HTML above change the name “Pete” to “Richard”.
document.querySelector("ul").firstElementChild.innerHTML="Richard"

// 2. Change each first name of the two <ul>'s to your name.

document.querySelector("ul").firstElementChild.innerHTML="Shmuel"
document.querySelector("ul").lastElementChild.innerHTML="Shmuel"


// 3. At the end of each <ul> add a <li> that says “Hey students”.


let x = document.querySelectorAll("ul")
for (i=0; i<x.length; i++) {
    let text = document.createElement("li")
    text.innerText = "Hey Students"
    x[i].appendChild(text)
    
}

// 4 .Delete the name Sarah from the second <ul>.

let x = document.querySelectorAll("ul")
for (i=0; i<x.length; i++) {
    let text = document.createElement("li")
    text.innerText = "Hey Students"
    x[i].appendChild(text)
    
}
// 5. Bonus
//        Add a class called student_list to both of the <ul>'s.
//        Add the classes university and attendance to the first <ul>.

document.querySelectorAll("ul").calas


// Exercise 3 

// For the following exercise use the HTML presented above:

// 1. Add a “light blue” background color and some padding to the <div>.
// let div = querySelector('div')
// div.style.backgroundColor='blue'
// div.style.padding='20px'
// 2. Do not display the first name (John) in the list.
// 3. Add a border to the second name (Pete).
// 4. Change the font size of the whole body.
// Bonus: If the background color of the div is “light blue”, 
// alert “Hello x and y” (x and y are the users in the div).

