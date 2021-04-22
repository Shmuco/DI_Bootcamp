let listTask = []
let task = document.getElementById("taskname")
let i = 0

task.addEventListener("change",getText)

function getText(e) {
    console.log(e)
listTask.push(e.target.value)

}
let form = document.getElementsByTagName('form')[0]
form.addEventListener("submit", addTask)

function addTask() {
    form.reset()
    console.log(listTask);
    event.preventDefault();
    let newTask = document.createElement("div");
    newTask.classList.add("task")
    newTask.setAttribute("name","Task"+i)
    newTask.setAttribute("type","checkbox")

    
    let listTasks=document.getElementsByTagName("div")[1];
    listTasks.appendChild(newTask)
    let newCheackbox = document.createElement("input")
    newCheackbox.setAttribute("type", "checkbox")
    newCheackbox.setAttribute("id","task"+i );
    newTask.appendChild(newCheackbox)
    let newLable = document.createElement("lable")
    newLable.setAttribute("for","task"+i)
    newLable.innerHTML ='<i class="fas fa-times"></i>'+" "+listTask[i]
    newTask.appendChild(newLable)
    console.log(listTasks);
    console.log(newTask);
   
    i++
}