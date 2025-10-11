<?php
echo "Hola mundo!"

$name = "Luis";
$age = 17;
echo "Mi nombre es " . $name . " y tengo " . $age . " años."

$num1 = (int)readline("Numero 1:");
$num2 = (int)readline("Numero 2:");;

$operation = $num1+$num2;
echo "Suma: " . $operation . "\n";
$operation = $num1-$num2;
echo "Resta: " . $operation . "\n";
$operation = $num1*$num2;
echo "Multiplicacion: " . $operation . "\n";
$operation = $num1/$num2;
echo "Division: " . $operation . "\n";

$countries = ["mexico","venezuela","francia"];
foreach ($countries as $country){
    echo $country . "\n";
};

$age = (int)readline("Ingrese su edad: ");
if($age < 18){
    echo "Usted es menor de edad";
}else if($age>=18 && $age <65){
    echo "Usted es un adulto.";
}else{
    echo "Usted es un anciano.";
}

$mulnum = (int)readline("Ingrese un numero: ");
for($i=1;$i<=10;$i++){
    $result = $mulnum*$i;
    echo $mulnum . " x " . $i . " = " . $result . "\n";
}

$array = [1,2,3,4,5,6];
calcaverage($array);

function calcaverage($array){
    $value2 = 0;
    foreach($array as $value){
        $value2 = $value2 + $value;
    }
    $fvalue = $value2/count($array);
    echo $fvalue;
}

include 'incfile.php';
echo "···Include \n";
require 'reqfile.php';
echo "···Require \n";

?>