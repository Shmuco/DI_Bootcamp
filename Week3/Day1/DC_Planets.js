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

}