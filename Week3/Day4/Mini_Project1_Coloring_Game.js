let numberOfDivs = 0;
let fillcolor= null;

while (numberOfDivs < 18000) {
  let div = document.createElement("div");
  let canvas = document.getElementById("canvas");
  div.classList.add("grid-item");
  canvas.appendChild(div);
  div.addEventListener("mouseover", changeColor);
  function changeColor(event) {
    console.log(event);
    if (event.buttons == 1) {
        console.log(event.buttons)
      div.style.backgroundColor = fillcolor;
    }
  }
  numberOfDivs++;
}

let colors = ["red", "yellow", "green", "blue", "orange"];
for (i in colors) {
  let div2 = document.createElement("div");
  let colorchooser = document.getElementById("colorchooser");
  console.log(colorchooser);
  div2.classList.add("colorchooser");
  div2.setAttribute("name", colors[i])
  div2.style.backgroundColor = colors[i];
  div2.addEventListener("click", function(e){
      fillcolor=e.target.getAttribute("name")
     
      
  });
  console.log(div2);
  colorchooser.appendChild(div2);
}

let clear = document.getElementsByTagName("button")[0];
clear.addEventListener("click", function(){
    document.location.reload()
})
