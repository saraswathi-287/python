greenlyt = document.getElementById("green");
orangelyte = document.getElementById("orange");
redlyte = document.getElementById("red");

function green(){
    greenlyt.classList.add("green");
    orangelyt.classList.remove("orange")
    redlyt.classList.remove("red")
}

function orange(){
    orangelyt.classList.add("orange");
    greeenlyt.classList.remove("green")
    redlyt.classList.remove("red")
}

function red(){
    redlyt.classList.add("red");
    greenlyt.classList.remove("green")
    orangelyt.classList.remove("orange")
}
    
    