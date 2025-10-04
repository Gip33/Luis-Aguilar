<?php

##1
for($i=1;$i<=50;$i++){
    $oddpair = $i % 2;
    if($oddpair == 1){
        echo $i . " Impar.\n";
    }else{
        echo $i . " Par.\n";
    };
};

##2
$mulnumber = (int)readline("Ingrese un numero: ");
for($i=1;$i<=10;$i++){
    echo $mulnumber . " x " . $i . " = " . ($mulnumber*$i) . "\n";
};

##3
$tries = [];
$randnumber = mt_rand(1,50);
var_dump($randnumber);
$win = false;
$trycounter = 0;

while($win==false){
    $try = (int)readline("Adivine el numero (1-50): ");
    array_push($tries, $try);
    if($try==$randnumber){
        $win = true;
    };
};
echo "Adivinaste el numero. \nIntentos: \n\n";
foreach($tries as $eachtry){
    echo "Intento " . ($trycounter+1) . "| Numero: " . $eachtry . "\n";
    $trycounter+=1;
};

##4
$fcount = 0;
echo "Numeros impares: \n\n";
for($i=1;$i<=100;$i++){
    $odd = $i % 2;
    if($odd == 1){
        $fcount += $i;
        echo $i . "\n";
    };
};
echo "\nTotal sumado: " . $fcount;

##5
$age = (int)readline("Ingrese su edad para obtener su licencia de conducir: ");
if($age >= 18 && $age < 65){
    echo "Usted puede obtener una licencia."
}else{
    echo "Usted no puede obtener una licencia."
};

##6
$size = 0;

while($size <= 5){
    echo "#####\n";
    $size++;
};

##7
$numbervalue = (int)readline("Ingrese un numero: ");
if($numbervalue < 0){
    echo "El numero es negativo.";
}elseif($numbervalue > 0){
    echo "El numero es positivio.";
}else{
    echo "El numero es cero.";
};

##8
for($i=1;$i<=30;$i++){
    $sealand3 = $i % 3;
    $sealand5 = $i % 5;
    if($sealand3 == 0 && $sealand5 == 0){
        echo "TierraMar\n";
    }elseif($sealand3 == 0){
        echo "Tierra\n";
    }elseif($sealand5 == 0){
        echo "Mar\n";
    }else{
        echo $i . "\n";
    };
};

##9
$temp = (int)readline("Ingrese una temperatura: ");
if($temp <= 10){
    echo "La temperatura es fria.";
}elseif($temp <=25){
    echo "La temperatura es calida.";
}else{
    echo "La temperatura es caliente.";
};

##10
for($i=10;$i>0;$i--){
    echo $i . "\n";
};
echo "Feliz año nuevo.!"
?>