<?php

main();

function main() {
    while (true) {
        $StudentsandNotes = [
            ["name" => "Marco", "notes" => ["math" => 16, "engl" => 13, "chem" => 10]],
            ["name" => "Pedro", "notes" => ["math" => 10, "engl" => 15, "chem" => 6]],
            ["name" => "Suzy", "notes" => ["math" => 20, "engl" => 20, "chem" => 20]],
            ["name" => "Mike", "notes" => ["math" => 10, "engl" => 19, "chem" => 15]],
            ["name" => "Hector", "notes" => ["math" => 9, "engl" => 3, "chem" => 2]]
        ];

        echo "-----------------------------\n";
        echo "| SISTEMA DE CALIFICACIONES |\n";
        echo "-----------------------------\n";
        echo "| 1. Ver Estudiantes.       |\n";
        echo "| 2. Ver Promedios.         |\n";
        echo "| 3. Ver Estado general.    |\n";
        echo "-----------------------------\n";
        $menuoption = (int)readline("Elija una opcion: ");
        switch ($menuoption) {
            case 1:
                system('cls');
                students($StudentsandNotes);
                break;
            case 2:
                system('cls');
                average($StudentsandNotes);
                break;
            case 3:
                system('cls');
                state($StudentsandNotes);
                break;
            default:
                system('cls');
                echo "El numero ingresado no coincide con las opciones disponibles.\n";
        };
    };
};

function calcaverage($notesArray) {
    if (count($notesArray) === 0) return 0;
    
    $sum = array_sum($notesArray);
    $count = count($notesArray);
    
    return $sum / $count;
};

function students($names) {
    echo "-----------------------------\n";
    echo "|        ESTUDIANTES        |\n";
    echo "-----------------------------\n\n";
    echo "<--------------------------->\n";
    foreach ($names as $students) {
        echo "Nombre: " . $students["name"] . "\n";
        foreach ($students["notes"] as $subject => $note) {
            echo $subject . ": " . $note . "\n";
        };
        echo "<--------------------------->\n";
    };
    readline("Presione 'ENTER' para continuar.");
    system('cls');
};

function average($names) {
    echo "-----------------------------\n";
    echo "|        ESTUDIANTES        |\n";
    echo "-----------------------------\n\n";
    echo "<--------------------------->\n";

    $studentAverages = [];

    foreach ($names as $student) {
        $notes = array_values($student["notes"]);
        $studentAvg = calcaverage($notes);
        $studentAverages[] = $studentAvg;

        echo "Nombre: " . $student["name"] . "\t| Promedio: " . $studentAvg . "\n";
    };

    $overallAverage = calcaverage($studentAverages);
    echo "<--------------------------->\n";
    echo "El promedio general es: " . $overallAverage . "\n";

    readline("Presione 'ENTER' para continuar.");
    system('cls');
};

function state($names) {
    echo "-----------------------------\n";
    echo "|     ESTADO GENERAL        |\n";
    echo "-----------------------------\n\n";

    $studentAverages = [];

    foreach ($names as $student) {
        $notes = array_values($student["notes"]);
        $average = calcaverage($notes);
        $studentAverages[] = $average;

        $msg = "";
        $passed = false;
        if($average >= 10){
            $passed = true;
            $msg = "Aprobado";
        }else{
            $msg = "reprobado";
        };

        echo "Nombre: " . $student["name"] . "\n";
        echo "Promedio: " . $average . "\n";
        echo "Estado: " . $msg . "\n";
        echo "<--------------------------->\n";
    };
    
    $overallAverage = calcaverage($studentAverages);
    echo "Promedio general del grupo: " . $overallAverage . "\n";

    readline("Presione 'ENTER' para continuar.");
    system('cls');
};

?>
