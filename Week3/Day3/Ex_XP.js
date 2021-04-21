// Excercise 1

let box = document.getElementById("animate")
let margin = 0
let moveBack = 350

function move(){
    if (margin<350){
    box.style.marginLeft=margin+"px";
    box.style.marginTop=margin+"px";
    margin=margin+2
    
    
}
    else {if (moveBack>0){
        box.style.marginLeft=moveBack+"px";
        box.style.marginTop=moveBack+"px";
    moveBack=moveBack-2}
    else{margin=0;
    moveBack=350}
}
}

function myMove(){
    setInterval(move,10)
}


// Excercise 2
let dragBox = document.getElementById("dragbox")
dragBox.addEventListener("dragstart",dragStart)


let container = document.getElementById("box2")
container.addEventListener("dragenter", dragEnter)
container.addEventListener("drop", dragEnd)

function dragStart() {
   
}
function dragEnter() {console.log("enter")}
function dragEnd() { 
   this.append(dragBox)
}
