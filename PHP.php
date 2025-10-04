<?php

##1
$name = readline("Ingrese su nombre: ");

echo "Hola, " . $name;

##2
$number1 = (float)readline("Ingrese un numero: ");
$number2 = (float)readline("\nIngrese otro numero: ");

//echo "\n" . $number1 . "\n" . $number2;

echo "\nSuma: " . ($number1+$number2) . "\n";
echo "Resta: " . ($number1-$number2) . "\n";
echo "Multiplicacion: " . ($number1*$number2) . "\n";
echo "Division: " . ($number1/$number2) . "\n";

##3
$covertion = 0.91;
$money =  (float)readline("Ingrese una cantidad en dolares: ");
$money *= $covertion;
echo "Su cantidad en euros: " . $money;

##4
$age = (int)readline("Ingrese su edad: ");
if($age>=18){
    echo "Usted es mayor de edad.";
}else{
    echo "Usted es menor de edad.";
};

##5
$oddpair = (int)readline("Ingrese un numero: ");
$oddpairfinal = $oddpair % 2;
if($oddpairfinal == 0){
    echo $oddpair . " es un numero par.";
} else{
    echo$oddpair . " es un numero impar.";
};

##6
$lifestage = (int)readline("Ingrese su edad: ");
if($lifestage < 13){
    echo "Usted es un niño.";
}elseif($lifestage < 18){
    echo "Usted es un adolescente.";
}elseif($lifestage < 50){
    echo "Usted es un adulto.";
}else{
    echo "Usted es un adulto mayor.";
};

##7
$user = "user123";
$password = "12345";
echo "Usuario: " . $user . "\nContraseña: " . $password;
$userlogin = readline("\n\nIngrese su usuario: ");
$passwordlogin = readline("\nIngrese su contraseña: ");
if($user == $userlogin && $password == $passwordlogin){
    echo "Contraseña y Usuario correctos.";
}else{
    echo "Contraseña o Usuario incorrectos.";
};

##8
$pay = (float)readline("Ingrese el precio de su compra: ");
if($pay < 50){
    echo "Compra hecha con exito.";
}elseif($pay < 100){
    echo "Compra hecha con exito, se ha aplicado un 5% de descuento.\n";
    $price = $pay - ($pay*0.05);
    echo "Precio final: " . $price;
}else{
    echo "Compra hecha con exito, se ha aplicado un 10% de descuento.\n";
    $price = $pay - ($pay*0.10);
    echo "Precio final: " . $price;
};

##9
$day = (int)readline("Ingrese un numero del 1 al 7: ");
switch($day){
    case 1:
        echo "Es Lunes.";
        break;
    case 2:
        echo "Es Martes.";
        break;
    case 3:
        echo "Es Miercoles.";
        break;
    case 4:
        echo "Es Jueves.";
        break;
    case 5:
        echo "Es Viernes.";
        break;
    case 6:
        echo "Es Sabado.";
        break;
    case 7:
        echo "Es Domingo.";
        break;
    default:
        echo "Numero no valido.";
};

##10
$note = (float)readline("Ingrese su nota: ");
if($note >= 60){
    echo "Usted esta aprobado.";
}else{
    echo "Usted esta reprobado.";
};
?>