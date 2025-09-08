import os
os.system('cls')

# Hard Level (No es dificil, profe, me engaño >:c)
exit = False

while exit == False:
    print("\n\t¡Bienvenido!")
    print("\nElije una de las siguientes opciones:")
    print("\n\n1. 🥇 El Mayor de Tres Numeros")
    print("2. 💪 Calculadora de IMC")
    print("3. 📦 Calculadora de Costos de Envio")
    print("4. 🔬 Resolucion de Ecuacion Cuadratica")
    print("5. 🗿📄✂  Juego de Piedra, Papel o Tijeras")
    print("6. Salir")
    option = int(input("\n\n\tIngrese el numero de la opcion que desea: "))

    if option == 1:
        os.system('cls')
        print("\n\t🥇 El Mayor de Tres Numeros")
        print("\nIngrese tres numeros, el programa decidira cual es el mayor de entre ellos.")
        num1 = int(input("\n\tPrimer Numero: "))
        num2 = int(input("\n\tSegundo Numero: "))
        num3 = int(input("\n\tTercero Numero: "))

        if num1 > num2 and num1 > num3:
            print(f"\n\n{num1} Es el mayor de los 3.")
            print("\nLos numeros dados se ordenan de mayor a menor de esta manera: ")
            if num2 >= num3:
                print(f"\n\t\t{num1} > {num2} > {num3}")
            else:
                print(f"\n\t\t{num1} > {num3} > {num2}")
        elif num2 > num1 and num2 > num3:
            print(f"\n\n{num2} Es el mayor de los 3.")
            print("\nLos numeros dados se ordenan de mayor a menor de esta manera: ")
            if num1 >= num3:
                print(f"\n\t\t{num2} > {num1} > {num3}")
            else:
                print(f"\n\t\t{num2} > {num3} > {num1}")
        elif num3 > num1 and num3 > num2:
            print(f"\n\n{num3} Es el mayor de los 3.")
            print("\nLos numeros dados se ordenan de mayor a menor de esta manera: ")
            if num1 >= num2:
                print(f"\n\t\t{num3} > {num1} > {num2}")
            else:
                print(f"\n\t\t{num3} > {num2} > {num1}")
        else:
            print("\n\nTodos los numeros son iguales")
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
        print("\n\t💪 Calculadora de IMC")
        print("\nIngrese su peso y su altura, solo ingrese el numero, el programa le dira su Indice de Masa Corporal.")
        weight = float(input("\n\tIngrese su peso: "))
        height = float(input("\n\tIngrese su altura: "))
        imc = weight / (height**2)

        if imc <= 18.49:
            print("\n\tSu peso es bajo.")
        elif imc > 18.49 and imc < 25:
            print("\n\tSu peso es normal.")
        elif imc >= 25 and imc < 30:
            print("\n\tUsted tiene sobrepeso.")
        elif imc >= 30 and imc < 35:
            print("\n\tUsted tiene obesidad leve.")
        elif imc >= 35 and imc < 40:
            print("\n\tUsted tiene obesidad media.")
        else:
            print("\n\nUsted tiene obesidad morbida")
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
        print("\n\t📦 Calculadora de Costos de Envio")
        print("\n\nA que distancia se enviara el paquete?")
        print("\nEn su misma ciudad (0-100 km). Digite 'LOCAL'")
        print("\nFuera de su ciudad (100-1000 km). Digite 'NACIONAL'")
        print("\nFuera del pais. Digite 'INTERNACIONAL'")
        print("\n\t(En envios nacionales, se aplica un descuento del 10% si el peso es mayor a 50kg.)")
        print("\t(En envios internacionales, se aplica un descuento del 20% si el peso es mayor a 100kg.)")
        shipping = input("\n\tIngrese el tipo de envio: ").lower()
        print("\n\nCual es el peso del paquete?")
        weight = float(input("\n\tIngrese el peso del paquete: "))
        if shipping == "local":
            cost = weight * 1.5
        elif shipping == "nacional":
            cost = weight * 3
        elif shipping == "internacional":
            cost = weight * 6
        else:
            print("\n¡Opcion no valida. Por favor, intente de nuevo!")
            input()
            os.system('cls')
        
        if shipping == "local":
            print(f"\nEl costo de envio local por el paquete es de: ${cost}")
        elif shipping == "nacional":
            if weight >= 50:
                cost *= 0.9
                print(f"\nEl costo de envio nacional por el paquete es de: ${cost} (10% de descuento aplicado)")
            else:
                print(f"\nEl costo de envio nacional por el paquete es de: ${cost}")
        elif shipping == "internacional":
            if weight >= 100:
                cost *= 0.8
                print(f"\nEl costo de envio internacional por el paquete es de: ${cost} (20% de descuento aplicado)")
            else:
                print(f"\nEl costo de envio internacional por el paquete es de: ${cost}")
        else:
            print("\n¡Opcion no valida. Por favor, intente de nuevo!")
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

    elif option == 4:
        os.system('cls')
        print("\n\t🔬 Resolucion de Ecuacion Cuadratica")
        print("\nIngrese los valores de a, b y c para resolver la ecuacion.")
        a = float(input("\n\tIngrese el valor de a: "))
        b = float(input("\n\tIngrese el valor de b: "))
        c = float(input("\n\tIngrese el valor de c: "))

        d = (b**2) - 4 * (a * c)
        if d < 0:
            print("\nLa ecuacion no tiene solucion en los numeros reales.")
        elif d == 0:
            x = -b / (2 * a)
            print(f"\nLa ecuacion tiene una solucion real: {x}")
        else:
            x1 = (-b + d**0.5) / (2 * a)
            x2 = (-b - d**0.5) / (2 * a)
            print(f"\nLa ecuacion tiene dos soluciones reales: {x1} y {x2}.")
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
        exit2 = False
        while exit2 == False:
            print("\n\t🗿📄✂  Juego de Piedra, Papel o Tijeras")
            print("\nJugador 1, ingrese su eleccion PIEDRA, PAPEL o TIJERAS: ")
            player1 = input("\n\tJugador 1: ").lower()
            os.system('cls')
            print("\nJugador 2, ingrese su eleccion PIEDRA, PAPEL o TIJERAS: ")
            player2 = input("\n\tJugador 2: ").lower()
            if player1 == player2:
                print("\n\n¡Es un empate!")
            elif (player1 == "piedra" and player2 == "tijeras") or (player1 == "tijeras" and player2 == "papel") or (player1 == "papel" and player2 == "piedra"):
                print("\n\n¡Jugador 1 gana!")
            elif (player2 == "piedra" and player1 == "tijeras") or (player2 == "tijeras" and player1 == "papel") or (player2 == "papel" and player1 == "piedra"):
                print("\n\n¡Jugador 2 gana!")
            else:
                print("\n¡Opcion no valida. Por favor, intente de nuevo!")
                input()
                os.system('cls')
            out = input("\nQuiere jugar otra vez? (SI/NO) : ").lower()
            if out == "si":
                os.system('cls')
            elif out == "no":
                exit2 = True
            else:
                print("\n¡Opcion no valida. Por favor, intente de nuevo!")
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

    elif option == 6:
        exit = True
        print("\n\t¡Gracias por usar el programa! ¡Hasta luego!")
        input()
    else:
        os.system('cls')
        print("\n¡Opcion no valida. Por favor, intente de nuevo!")