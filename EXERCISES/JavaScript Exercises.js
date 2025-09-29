const prompt = require('prompt-sync')(); 
console.clear();
var exit = false;

while(exit == false){
    console.log("EJERCICIOS");
    console.log("1. Saludo personalizado.");
    console.log("2. Conversor de moneda.");
    console.log("3. Comparador de numeros.");
    console.log("4. Acceso a club nocturno.");
    console.log("5. Dia laboral o fin de semana.");
    console.log("6. Tabla de multiplicar.");
    console.log("7. Cuenta regresiva.");
    console.log("8. Validador de contraseña.");
    console.log("9. Sumador acumulativo.");
    console.log("10. FizzBuzz clasico.");
    var menu = prompt("Ingrese un numero: ");
    menu = Number(menu);
    console.clear();
    switch(menu){
        case 1:
            name = prompt("Ingrese su nombre: ");
            console.log(`Hola ${name}!`);
            prompt("Precione 'ENTER' para volver al menu: ");
            break;
        case 2:
            const exrate = 0.85
            var money = parseFloat(prompt("Ingrese una cantidad de dinero en dolares: "));
            money = money*exrate;
            console.log(`Este es su valor en Euros: ${money}`)
            prompt("Precione 'ENTER' para volver al menu: ");
            break;
        case 3:
            var number1 = prompt("Ingrese un numero: ");
            var number2 = prompt("Ingrese otro numero: ");
            if(number1 > number2){
                console.log(`${number1} es mayor que ${number2}.`);
            }else if(number1 < number2){
                console.log(`${number2} es mayor que ${number1}.`);
            }else{
                console.log("Ambos numeros son iguales.")
            };
            prompt("Precione 'ENTER' para volver al menu: ");
            break;
        case 4:
            var age = Number(prompt("Ingrese su edad: "));
            console.log("El club nocturno pide $20 para la entrada");
            var cash = Number(prompt("Ingrese cuanto dinero tiene: "));
            if(age >= 18 && cash >= 20){
                console.log("Usted tiene la edad y el dinero suficiente para entrar.");
            }else if(age < 18){
                console.log("Usted no tiene la edad suficiente ara entrar.")
            }else{
                console.log("Usted no tiene suficiente dinero para entrar.")
            };
            prompt("Precione 'ENTER' para volver al menu: ");
            break;
        case 5:
            var day = prompt("Ingrese el nombre de un dia: ").toLowerCase();
            switch(day) {
                case "lunes":
                case "martes":
                case "miercoles":
                case "jueves":
                case "viernes":
                    console.log(`${day} es un día laboral`);
                    break;

                case "sabado":
                case "domingo":
                    console.log(`${day} es un fin de semana`);
                    break;

                default:
                    console.log("Día no válido");
            };
            prompt("Precione 'ENTER' para volver al menu: ");
            break;
        case 6:
            var multnum = Number(prompt("Ingrese un numero para ver su tabla de multiplicar: "));
            var ognum = multnum;
            for(i=1;i<=10;i++){
                multnum = ognum*i;
                console.log(`${ognum} x ${i} = ${multnum}`);
            };
            prompt("Precione 'ENTER' para volver al menu: ");
            break;
        case 7:
            var backwards = Number(prompt("Ingrese un numero: "));
            for(i=backwards;i>=0;i--){
                console.log(i);
            };
            prompt("Precione 'ENTER' para volver al menu: ");
            break;
        case 8:
            var setpassword = prompt("Escriba su contraseña: ");
            do{
                var seepassword = prompt("Escriba su contraseña nuevamente: ");
            }while(seepassword!=setpassword);
            prompt("Precione 'ENTER' para volver al menu: ");
            break;
        case 9:
            console.log("El programa sumara todos los numeros que digite. Para salir digite '0'.");
            var fsum = 0;
            while(true){
                var plusnum = Number(prompt("Digite un numero: "));
                fsum += plusnum;
                if(plusnum == 0){
                    prompt("Precione 'ENTER' para volver al menu: ");
                    break;
                }else{
                    console.log(fsum);
                };
            };
            break;
        case 10:
            for(i=1;i<=100;i++){
                module3 = i % 3
                module5 = i % 5
                if(module3==0 && module5==0){
                    console.log("FizzBuzz");
                }else if(module3==0){
                    console.log("Fizz");
                }else if(module5==0){
                    console.log("Buzz")
                }else{
                    console.log(i);
                };
            };
            prompt("Precione 'ENTER' para volver al menu: ");
            break;
    };
    console.clear();
};