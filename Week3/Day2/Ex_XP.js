// Excercise 1


// 1. Using DOM methods, remove the last paragraph in the <article> tag from the DOM.
let ps = document.getElementsByTagName("p");
ps[ps.length-2].remove()

// 2. Add an event listener which will change the background color of the h2 tag from the DOM when clicked on.
let h2 = document.getElementsByTagName("h2")[0]
h2.addEventListener("mouseover", changeColor);

function changeColor(){
    h2.style.backgroundColor="yellow"
}
// 3. Set the font size of the h1 tag to a random pixel size between 0 to 100.(Check out this documentation)
let h1 = document.getElementsByTagName("h1")[0]
    h1.addEventListener("click", function(){
        h1.style.fontSize=`${Math.floor(Math.random() * 101)}px`
    })
// 4. Add an event listener which will hide the h3 when it’s clicked on (use the display property).
let h3 = document.getElementsByTagName("h3")[0]
h3.addEventListener("click", function(){
    h3.style.display="none"
})


// 5. Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
let but = document.getElementsByTagName("button")[0]
but.addEventListener("click", function(){
    let ps = document.getElementsByTagName("p")
    
    for (p of ps){
        p.style.fontWeight="bold"
    }
})

// 6. When the “Submit” button of the form is clicked:
//     get the values of the input tags
//     make sure that they are not empty,
//     then append them to a HTML table, in the div, below the form.


// 7. When you hoover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)
let par2 = document.getElementsByTagName("p")[1]
par2.addEventListener("mouseover", function(){
    
})

// // Excercise 2
// function getBold_items() {
//     bold = document.getElementsByTagName("strong")
// }

// function highlight (){
//     getBold_items()
    
//     for (words of bold)
//     words.style.color="blue";}

// function return_normal(){
//     getBold_items()
//     for (words of bold)
//     words.style.color="black"
// }

// let p = document.getElementsByTagName("p")[3]
// p.addEventListener("mouseover", highlight)
// p.addEventListener("mouseout", return_normal)


// // Excercise 3
// let values = { }
// let inputs = document.getElementsByTagName("input");
// for (input of inputs) {
//     input.addEventListener("change", function(e) {
//         values = {
//             ...values,
//             [e.target.name]: e.target.value
//         }
//         console.log(values);
//     })
// }
// let form = document.getElementsByTagName('form')[0];
// form.addEventListener('submit', function(e) {
//     e.preventDefault();
//     for 
    
// })

// let logout = document.createElement("p")
// li.innerText = "Log Out"
// document.querySelector("ul").appendChild(logout)
