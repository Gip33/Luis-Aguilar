const name = "Luis"
console.log("Hola, mi nombre es: " + name)

var num1 = Number(prompt("Numero 1: "));
var num2 = Number(prompt("Numero 2: "));

var operation = num1+num2;
console.log("Suma: " + operation);
var operation = num1-num2;
console.log("Resta: " + operation);
var operation = num1*num2;
console.log("Multiplicacion: " + operation);
var operation = num1/num2;
console.log("Division: " + operation);

object = {
    "name" : "Juan",
    "age" : 15,
    "email" : "juan123@email"
};
console.log(object);
console.log(object["email"]);

var value = Number(prompt("Ingrese un numero: "));
if(value<50){
    alert("El numero es menor que 50.")
}else if(value=>50){
    alert("El numero es igual o mayor que 50.")
}

function Ivacalc(amount){
    const IVA = 0.21;
    amount = amount + (amount * IVA);
    return amount;
}
var amount = Number(prompt("Ingrese una cantidad: "));
var famount = Ivacalc(amount);
console.log('El precio final es ', famount);

var amount = Number(prompt("Ingrese una cantidad: "));
var famount = Ivacalc(amount);
console.log('El precio final es ', famount);


var number = prompt("Type a number: ");
var counter = 0;
while(counter<=number){
    if(counter===5){
        counter ++;
        continue;
    }
    console.log(counter);
    counter ++;
}

class rectangle{

    constructor(base,height){
        this.base = base;
        this.height = height;
    }
    calcarea(){
        return this.base*this.height
    }
}

var height = Number(prompt("Ingrese la altura: "));
var base = Number(prompt("Ingrese la base: "));
const newrectangle = new rectangle(base,height);
console.log("Area: ", newrectangle.calcarea());