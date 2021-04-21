function createStory (){
    let inputs = document.getElementsByTagName("input");
    let story_list = [];
    for (input in inputs){
        inputs[input].setAttribute("required", true);
        console.log(inputs[input]);
    let value = inputs[input].value
console.log(inputs[input]);   } }