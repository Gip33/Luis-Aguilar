const prompt = require('prompt-sync')(); 
console.clear();

var shoppinglist = [];
//[name, amount, value]

menu()
function menu (){
    menuexit = false;
    while(menuexit == false){
        console.log("----------------------------------");
        console.log("|Bienvenido al carrito de compras|");
        console.log("----------------------------------");
        console.log("|1. Agregar.                     |");
        console.log("|2. Mostrar.                     |");
        console.log("|3. Eliminar.                    |");
        console.log("|4. Calcular.                    |");
        console.log("|5. Salir.                       |");
        console.log("----------------------------------");
        var menuslct = Number(prompt("Elija una opcion: "));

        switch(menuslct){
            case 1:
             console.clear();
                add();
                break;
            case 2:
                console.clear();
                show();
                break;
            case 3:
                console.clear();
                remove();
                break;
            case 4:
                console.clear();
                calc();
                break;
            case 5:
                console.log("----------------------------------");
                console.log("|Gracias por utilizar el programa|");
                console.log("----------------------------------");
                menuexit = true;
                prompt("Ingrese 'ENTER' para continuar: ");
                break;
            default:
                console.log("Lo que ingreso no es una opcion valida!");
                prompt("Ingrese 'ENTER' para continuar: ");
                console.clear();
        };
    };
};

function add (){
    
    console.log("---------------------------------------");
    console.log("|           Agregar productos         |");
    console.log("---------------------------------------");
    console.log("|         Para salir digite '0'       |");
    console.log("|       como nombre del producto      |");
    console.log("---------------------------------------");

    while(true){
        console.log("")
        var pname  = prompt("Nombre del producto: ");
        if(pname === "0"){
            console.clear();
            break;
        };
        var pvalue = Number(prompt("Precio del producto: "));
        var pamount = Number(prompt("Cantidad de productos: "));
        
        var index = shoppinglist.findIndex(item => item[0] === pname);
        if(index !== -1){
            shoppinglist[index][1] += pamount;
        }else{
            shoppinglist.push([pname,pamount,pvalue]);
        };

        var size = shoppinglist.length;
        console.log("\nSu carrito:");
        for(i=0;i<size;i++){
            var product = shoppinglist[i];
            console.log(`${product[0]} | Cantidad: ${product[1]} | Precio: $${product[2]}`);
        };
    };
};

function show (){
    console.log("-------------------------------------------------");
    console.log("|                   Su Carrito                  |");
    console.log("-------------------------------------------------");
    
    var size = shoppinglist.length;

    if(size === 0){
        console.log("El carrito esta vacio.");
    }else{
        for(i=0;i<size;i++){
            var product = shoppinglist[i];
            console.log(`${product[0]} | Cantidad: ${product[1]} | Precio: $${product[2]}`);
        };
    };
        
    prompt("\n\nIngrese 'ENTER' para continuar: ");
    console.clear();
};

function remove (){
    console.log("---------------------------------------");
    console.log("|          Eliminar productos         |");
    console.log("---------------------------------------");
    console.log("|         Para salir digite '0'       |");
    console.log("|       como nombre del producto      |");
    console.log("---------------------------------------");

    while(true){

        var size = shoppinglist.length;
        console.log("\nSu carrito:");
        for(i=0;i<size;i++){
            var product = shoppinglist[i];
            console.log(`${product[0]} | Cantidad: ${product[1]} | Precio: $${product[2]}`);
        };

        console.log("")
        var pname  = prompt("Nombre del producto: ");
        if(pname === "0"){
            console.clear();
            break;
        };

        var size = shoppinglist.length;
        for(i=0;i<size;i++){
            if(shoppinglist[i][0] === pname){
                shoppinglist.splice(i, 1);
                console.log(`${pname} ha sido eliminado del carrito.`);
                var found = true;
                break;
            };
        };

        if(found != true){
            console.log(`${pname} no encontrado en la lista.`);
        }; 
    };
};

function calc (){
    var size = shoppinglist.length;

    console.log("\nSu carrito:");
    for(i=0;i<size;i++){
        var product = shoppinglist[i];
        console.log(`${product[0]} | Cantidad: ${product[1]} | Precio: $${product[2]}`);
    };

    var fprice = 0;
    for(i=0;i<size;i++){
        var listamount = shoppinglist[i][1];
        var listvalue = shoppinglist[i][2];
        //console.log(listamount," ", listvalue," ", fprice)
        fprice = fprice + (listamount * listvalue);
    };
    console.log(`El valor final de la compra es: $${fprice}`)
    prompt("\n\nIngrese 'ENTER' para continuar: ");
    console.clear();
};