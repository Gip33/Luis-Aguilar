import os
os.system('cls')

# Easy Level
exit = False

while exit == False:
    print("\n\t¡Bienvenido!")
    print("\nElije una de las siguientes opciones:")
    print("\n\n1. 📐 Calculadora de Area de Rectangulo")
    print("2. 🌡  Conversor de Temperatura")
    print("3. ✍  Concatenacion de Cadenas")
    print("4. 🔢 Verificacion de Numero Par o Impar")
    print("5. 🗳  Elegibilidad para Votar")
    print("6. ⚖  Comparador de Numeros")
    print("7. 🧠 Operadores Logicos")
    print("8. 🔐 Verificacion de Contraseña Simple")
    print("9. Salir")
    option = int(input("\n\n\tIngrese el numero de la opcion que desea: "))

    if option == 1:
        os.system('cls')
        print("\n\t📐 Calculadora de Area de Rectangulo")
        base = float(input("\n\n↔ Ingrese la base del rectangulo: "))
        height = float(input("\n↕ Ingrese la altura del rectangulo: "))
        area = base * height
        print(f"\n\t◻ El area del rectangulo es: {area}")
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
        print("\n\t🌡 Conversor de Temperatura")
        print("\n1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")
        conversion_option = float(input("\n\n\tIngrese el numero de la opcion que desea: "))
        if conversion_option == 1:
            celsius = float(input("\n\n\tIngrese la temperatura en Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"\n\t🌡 La temperatura en Fahrenheit es: {fahrenheit:.2f}°F")
            input_option = input("\nQuiere volver al menu principal o salir del programa? (MENU/SALIR) : ").lower()
            if input_option == "menu":
                os.system('cls')
            elif input_option == "salir":
                exit = True
                print("\n\t¡Gracias por usar el programa! ¡Hasta luego!")
            else:
                print("\n¡Opcion no valida. Por favor, intente de nuevo!")
                input()
                os.system('cls')

        elif conversion_option == 2:
            fahrenheit = float(input("\n\n\tIngrese la temperatura en Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"\n\t🌡 La temperatura en Celsius es: {celsius:.2f}°C")
            input_option = input("\nQuiere volver al menu principal o salir del programa? (MENU/SALIR) : ").lower()
            if input_option == "menu":
                os.system('cls')
            elif input_option == "salir":
                exit = True
                print("\n\t¡Gracias por usar el programa! ¡Hasta luego!")
        else:
            print("\n¡Opcion no valida. Por favor, intente de nuevo!")
            input()
            os.system('cls')

    elif option == 3:
        os.system('cls')
        print("\n\t✍  Concatenacion de Cadenas")
        string1 = input("\n\nIngrese su nombre: ")
        string2 = input("\nIngrese su apellido: ")
        final_string = string1 + " " + string2
        print(f"\n\t✍  Asi que te llamas {final_string}?")
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
        print("\n\t🔢 Verificador de Número Par o Impar")
        print("Ingrese un numero, el programa identificara si es PAR o INPAR")
        number = int(input("\n\nIngrese su numero: "))
        result = number % 2
        if result == 0:
            print(f"\nEl numero {number} es PAR")
        else:
            print(f"\nEl numero {number} es INPAR")
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
        print("\n\t🗳 Elegibilidad para Votar")
        print("\nUsuario, para poder votar usted requiere ser mayor de edad (+18).")
        vote_age = int(input("\n\nDigite su edad: "))
        if vote_age >= 18 :
            print("\n\tUsted esta en el rango de edad requerido para votar, puede proceder!")
        else:
            print("\n\tUsted no cumple con la edad requerida. >:(")
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
        print("\n\t⚖ Comparador de Numeros")
        num1 = int(input("\n\nEscriba el primer numero a comparar: "))
        num2 = int(input("\nEscriba el segundo numero a comparar: "))
        if num1 == num2:
            print(f"\n\tAmbos numeros son iguales")
        elif num1 > num2:
            print(f"\n\t{num1} es mayor que {num2}.")
        else:
            print(f"\n\t{num2} es mayor que {num1}.")
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

    elif option == 7:
        os.system('cls')
        print("\n\t🧠 Operadores Logicos")
        print("\nEscriba un numero, el programa detectara si esta en un rango entre 10 y 20")
        rangenum = int(input("\n\nEscriba un numero: "))
        if rangenum >= 10 and rangenum <= 20:
            print("\n\tEl numero esta entre el rango de 10 y 20")
        else:
            print("\n\tEl numero no esta en el rango entre 10 y 20")
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
        os.system('cls')

        loginexit1 = False
        while loginexit1 == False:
            print("\n\t🔐 Verificacion de Contraseña Simple")
            user1 = input("\n\nIngrese su usuario: ").lower()
            pasword1 = input("\nIngrese su contraseña: ").lower()
            pasword2 = input("\nIngrese denuevo su contraseña: ").lower()

            if pasword1 == pasword2:
                print("\n\tUsuario creado correctamente. Presione ENTER para continuar")
                input()
                os.system('cls')
                loginexit2 = False

                while loginexit2 == False:
                    print("\n\t➡ Login")
                    user2 = input("\n\nIngrese su usuario: ").lower()
                    pasword3 = input("\nIngrese su contraseña: ").lower()
                    if user2 == user1 and pasword3 == pasword1:
                        print("\n\t✅ Ha iniciado sesion correctamente!")
                        loginexit2 = True
                        loginexit1 = True
                    else:
                        print("\n\t⛔ El usuario o contraseña son invalidos.")
                        input()
                        os.system('cls')
            else:
                print("\n\tLas contraseñas no son iguales.")
                print("\n\t\tIntente nuevamente!")
                input()
                os.system('cls')

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

    elif option == 9:
        exit = True
        print("\n\t¡Gracias por usar el programa! ¡Hasta luego!")
        input()
    else:
        os.system('cls')
        print("\n¡Opcion no valida. Por favor, intente de nuevo!")