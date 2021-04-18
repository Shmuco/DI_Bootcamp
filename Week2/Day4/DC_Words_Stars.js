var words = prompt("Please words seperated by commas ")
var string = words.split(",")
var maxLength = 0
var stars="*"
console.log(string)


for (let i=0 ; i<string.length; i++) {
    if (string[i].length > maxLength) {
        maxLength = string[i].length
    }

}
console.log(stars.repeat(maxLength+4))
for (words in string){
console.log("* "+ string[words]+" ".repeat(maxLength-string[words].length)+" *" )}
console.log(stars.repeat(maxLength+4))


