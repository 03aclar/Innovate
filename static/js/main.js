function funcExample () {
    console.log("hello world");
};

let my_name = "Ash" 
    
const my_last_name = "Clarke"

if (my_name === "Ash") {
console.log(`hello, ${my_name}!`)
} else {
    console.log("you're not Ash")
}

function reallygoodfunction (num1, num2) {
    let result = num1 + num2
    return result
}

function taskHider () {
    let element = document.getElementById("task-box")
    element.classList.toggle("hidden")
}