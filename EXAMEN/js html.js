function textchange(){
    const text = document.getElementById("OGtext");
    text.innerText = "El texto cambio";
}
function colorlist(){
    const list = document.getElementById("colors");
    const colors = ["red", "green", "yellow", "black"];

    for(i=0;i<colors.length;i++){
        const newentry = document.createElement("li");
        newentry.innerText = colors[i];
        list.appendChild(newentry);
    }
}
colorlist()

function lowertext(){
    const title = document.getElementById("titlechange");
    var currentSize = parseFloat(title.style.fontSize)
    title.style.fontSize = (currentSize-2) + 'px';
}
function uppertext(){
    const title = document.getElementById("titlechange");
    var currentSize = parseFloat(title.style.fontSize)
    title.style.fontSize = (currentSize+2) + 'px';
}

const form = document.getElementById('Form');

function send(event) {
    event.preventDefault();

    const nameInput = document.getElementById('name').value;
    const emailInput = document.getElementById('email').value;

    const Data = {
        name: nameInput,
        email: emailInput,
    };

    console.log(Data);

    form.reset();
}

form.addEventListener('submit', send);

const listElement = document.getElementById("addremove");
const addInput = document.getElementById("addbutton");

function plustext() {
    const itemText = addInput.value.trim();

    const newItem = document.createElement("li");
    newItem.textContent = itemText;
    listElement.appendChild(newItem);
    addInput.value = "";

    const newButton = document.createElement("button");
    newButton.innerText = "Borrar";

    newButton.onclick = function(){
        listElement.removeChild(newItem);
    }
    newItem.appendChild(newButton);

}

const clock = document.getElementById('clock');

function updateclock() {
    const time = new Date();
    
    const digitlimit = { 
        hour: '2-digit', 
        minute: '2-digit', 
        second: '2-digit' 
    };

    const nowtime = time.toLocaleTimeString('es-ES', digitlimit);
    clock.innerText = nowtime;
}
updateclock();
setInterval(updateclock, 1000);

const mainImage = document.getElementById('Mainimg');
const otherImages = document.querySelectorAll('.otherimg');


function swapSrc() {
    const clickedImage = this; 
            
    mainImage.src = clickedImage.src;
}

otherImages.forEach(image => {
    image.addEventListener('click', swapSrc);
});