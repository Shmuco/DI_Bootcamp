let planets =["earth", "jupiter", "neptune", "saturn", "mars", "uranus","venus","mercury"]
for (i in planets) {
    let div = document.createElement("div")
    div.classList.add(planets[i], "planet")
    div.innerHTML= planets[i]   
    document.body.appendChild(div)
    
        if (planets[i]=="mars"){
            let x =0 
        while (x<3){
        let moon = document.createElement("div")
        moon.classList.add("moon") 
        document.body.appendChild(moon)
        x++
        
    }
    
}

if (planets[i]=="earth"){
    let x =0 
while (x<1){
let moon = document.createElement("div")
moon.classList.add("moon") 
document.body.appendChild(moon)
x++

}

}

if (planets[i]=="jupiter"){
    let x =0 
while (x<79){
let moon = document.createElement("div")
moon.classList.add("moon") 
document.body.appendChild(moon)
x++

}

}
if (planets[i]=="neptune"){
    let x =0 
while (x<14){
let moon = document.createElement("div")
moon.classList.add("moon") 
document.body.appendChild(moon)
x++

}

}
if (planets[i]=="saturn"){
    let x =0 
while (x<62){
let moon = document.createElement("div")
moon.classList.add("moon") 
document.body.appendChild(moon)
x++

}

}
if (planets[i]=="uranus"){
    let x =0 
while (x<27){
let moon = document.createElement("div")
moon.classList.add("moon") 
document.body.appendChild(moon)
x++

}

}
}