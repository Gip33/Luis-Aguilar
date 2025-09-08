import os
os.system('cls')

# Medium Level
exit = False

while exit == False:
    print("\n\t¡Bienvenido!")
    print("\nElije una de las siguientes opciones:")
    print("\n\n1. 💰 Calculadora de Descuento")
    print("2.  ± Clasificador de Numeros")
    print("3. 🗓  Año Bisiesto")
    print("4. 🎓 Calculadora de Calificaciones")
    print("5. 🅰  Verificador de Vocal o Consonante")
    print("6. 📋  Seleccion de Menu")
    print("7. 🔺 Tipo de Triangulo")
    print("8. Salir")
    option = int(input("\n\n\tIngrese el numero de la opcion que desea: "))

    if option == 1:
        os.system('cls')
        print("\n\t💰 Calculadora de Descuento")
        print("\nSi el precio de su compra supera los 100$ se aplicara un 15% de descuento")
        num1 = int(input("\n\nDigite el precio a procesar: "))
        if num1 >= 100:
            num2 = 15 * num1 / 100
            fprice = float(num1-num2)
            print(f"\nSu compra supera los 100$, se aplicara un descuento del 15%.")
        else:
            fprice = num1
            print(f"\nSu compra no supera los 100$, no se aplicara el descuento.")
        print(f"\n\tEl precio final es de: {fprice:.2f}$")
        input_option = input("\nQuiere volver al menu principal o salir del programa? (MENU/SALIR) : ").lower()
        if input_option == "menu":
            os.system('cls')
        elif input_option == "salir":
            exit = True
            print("\n\t¡Gracias por usar el programa! ¡Hasta luego!")
        else :
            print("\n¡Opcion no valida. Por favor, intente de nuevo!")
            input()
            os.system('cls')

    elif option == 2:
        os.system('cls')
        print("\n\t± Clasificador de Numeros")
        print("\nDigite un numero, el programa decidira si es positivo, negativo o cero.")
        num1 = float(input("\n\tDigite un numero: "))
        if num1 == 0:
            print(f"\nEl numero {num1} es igual a 0.")
        elif num1 < 0:
            print(f"\nEl numero {num1} es negativo.")
        else :
            print(f"\nEl numero {num1} es positivo.") 
        input_option = input("\nQuiere volver al menu principal o salir del programa? (MENU/SALIR) : ").lower()
        if input_option == "menu":
            os.system('cls')
        elif input_option == "salir":
            exit = True
            print("\n\t¡Gracias por usar el programa! ¡Hasta luego!")
        else :
            print("\n¡Opcion no valida. Por favor, intente de nuevo!")
            input()
            os.system('cls')

    elif option == 3:
        os.system('cls')
        print("\n\t🗓  Año Bisiesto")
        print("\nDigite un año, el programa decidira si es bisiesto o no.")
        year = int(input("\n\tDigite un año: "))
        fyear = year % 4
        if fyear == 0:
            print(f"\nEl año {year} es bisiesto.")
        else:
            print(f"\nEl año {year} no es bisiesto.")
        input_option = input("\nQuiere volver al menu principal o salir del programa? (MENU/SALIR) : ").lower()
        if input_option == "menu":
            os.system('cls')
        elif input_option == "salir":
            exit = True
            print("\n\t¡Gracias por usar el programa! ¡Hasta luego!")
        else :
            print("\n¡Opcion no valida. Por favor, intente de nuevo!")
            input()
            os.system('cls')

    elif option == 4:
        os.system('cls')
        print("\n\t🎓 Calculadora de Calificaciones")
        print("\nEstudiante, ingrese su calificacion en sistema 0-100, el programa le dara su nota en sistema A-F")
        note = float(input("\n\tIngrese su nota: "))
        if note >= 0 and note < 60:
            print(f"\nSu nota de {note} corresponde a una 'F'.")
        elif note >= 60 and note < 70:
            print(f"\nSu nota de {note} corresponde a una 'D'.")
        elif note >= 70 and note < 80:
            print(f"\nSu nota de {note} corresponde a una 'C'.")
        elif note >= 80 and note < 90:
            print(f"\nSu nota de {note} corresponde a una 'B'.")
        elif note >= 90 and note <= 100:
            print(f"\nSu nota de {note} corresponde a una 'A'.")
        else:
            print("\nSu nota no corresponde al sistema de calificacion 0-100, intente de nuevo.")
        input_option = input("\nQuiere volver al menu principal o salir del programa? (MENU/SALIR) : ").lower()
        if input_option == "menu":
            os.system('cls')
        elif input_option == "salir":
            exit = True
            print("\n\t¡Gracias por usar el programa! ¡Hasta luego!")
        else :
            print("\n¡Opcion no valida. Por favor, intente de nuevo!")
            input()
            os.system('cls')

    elif option == 5:
        os.system('cls')
        print("\n\t🅰  Verificador de Vocal o Consonante")
        print("\nIngrese una letra, el programa decidira si es una vocal o una consonante.")
        letter = input("\n\tIngrese una letra: ").lower()
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            print(f"\n\nLa letra {letter} es una vocal.")
        else:
            print(f"\n\nLa letra {letter} es una consonante.")
        input_option = input("\nQuiere volver al menu principal o salir del programa? (MENU/SALIR) : ").lower()
        if input_option == "menu":
            os.system('cls')
        elif input_option == "salir":
            exit = True
            print("\n\t¡Gracias por usar el programa! ¡Hasta luego!")
        else :
            print("\n¡Opcion no valida. Por favor, intente de nuevo!")
            input()
            os.system('cls')

    elif option == 6:
        os.system('cls')
        print("\n\t📋  Seleccion de Menu")
        print("\n\n\n\tBIENVENIDO AL MENU!")
        print("\nQue desea ver?")
        print("\n1. Un epico menu.")
        print("\n2. Los otros ejercicios que puso.")
        print("\n3. El codigo.")
        code = int(input("\n\tDigame pues, que numero de opcion elegira?: "))
        if code == 1:
            os.system('cls')
            print("\n\tYa lo vio, feliz?")
        elif code == 2:
            os.system('cls')
            print("\n\tPues devuelvase al menu principal, ahi estan.")
        elif code == 3:
            os.system('cls')
            print("\n\tYo creo que ya lo esta viendo o ya lo vio.")
        else:
            os.system('cls')
            print("\n\tQue fue? No lo puse con numeritos? Como puso algo que no era?")
        input_option = input("\nQuiere volver al menu principal o salir del programa? (MENU/SALIR) : ").lower()
        if input_option == "menu":
            os.system('cls')
        elif input_option == "salir":
            exit = True
            print("\n\t¡Gracias por usar el programa! ¡Hasta luego!")
        else :
            print("\n¡Opcion no valida. Por favor, intente de nuevo!")
            input()
            os.system('cls')
        #Cuando vi que tenia que hacer esto me rei un poco, no lo habia visto y ya habia hecho todos los faciles, los cuales tambien tienen el menu :v

    elif option == 7:
        os.system('cls')
        print("\n\t🔺 Tipo de Triangulo")
        print("\nIngrese las medidas de su triangulo, el programa le dira que tipo de triangulo es.")
        side1 = int(input("\n\tPrimer lado: "))
        side2 = int(input("\n\tSegundo lado: "))
        side3 = int(input("\n\tTercer lado: "))

        if side1 == side2 and side2 == side3:
            print("\nEl triangulo ingresado es Equilatero.")
        elif side1 == side2 or side1 == side3 or side2 == side3:
            print("\nEl triangulo ingresado es Isosceles.")
        elif side1 != side2 and side2 != side3:
            print("\nEl triangulo ingresado es Escaleno")
        else:
            print("\nLo ingresado no es valido!")
        input_option = input("\nQuiere volver al menu principal o salir del programa? (MENU/SALIR) : ").lower()
        if input_option == "menu":
            os.system('cls')
        elif input_option == "salir":
            exit = True
            print("\n\t¡Gracias por usar el programa! ¡Hasta luego!")
        else :
            print("\n¡Opcion no valida. Por favor, intente de nuevo!")
            input()
            os.system('cls')

    elif option == 8:
        exit = True
        print("\n\t¡Gracias por usar el programa! ¡Hasta luego!")
        input()
    else:
        os.system('cls')
        print("\n¡Opcion no valida. Por favor, intente de nuevo!")
        