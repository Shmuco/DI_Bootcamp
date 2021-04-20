// Excercise 1


// 1. Using DOM methods, remove the last paragraph in the <article> tag from the DOM.
// 2. Add an event listener which will change the background color of the h2 tag from the DOM when clicked on.
let h2 = document.getElementById("h2")
h2.addEventListener("mouseover", changeColor);

function changeColor(){
    h2.style.backgroundColor="yellow"
}
// 3. Set the font size of the h1 tag to a random pixel size between 0 to 100.(Check out this documentation)
// 4. Add an event listener which will hide the h3 when it’s clicked on (use the display property).
// 5. Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
// 6. When the “Submit” button of the form is clicked:
//     get the values of the input tags
//     make sure that they are not empty,
//     then append them to a HTML table, in the div, below the form.
// 7. When you hoover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)
