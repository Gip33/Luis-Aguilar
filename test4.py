import os
os.system('cls')

print("\n\n\t\t¡BIENVENIDO USUARIO!")

exit = False

while exit == False :
    print("\tDigite los dos numeros a utilizar: ")

    num1 = float(input("\n\tNUMERO 1: "))
    num2 = float(input("\n\tNUMERO 2: "))
    
    print("\n\t\t¿Que operacion desea realizar?")
    print("\tSUMA\n\tRESTA\n\tMULTIPLICACION\n\tDIVISION")
    op = input("\n\t\tSeleccione una opcion: ").lower()
    if op == "suma" :
        num3 = num1+num2
        print(f"\n\tEste es el resultado: {num3: .2f}")
        print("\n\n\t¿Quieres realizar una nueva operacion o salir de la calculadora?")
        exxit = input("\n\nElija 'NUEVA' o 'SALIR': ").lower()
        if exxit == "salir" :
            exit = True
        elif exxit == "nueva" :
            exxit = False
            os.system('cls')
        else :
            print("¡Opcion no valida, cerrando el sistema!")

    elif op == "resta" :
        num3 = num1-num2
        print(f"\n\tEste es el resultado: {num3: .2f}")
        print("\n\n\t¿Quieres realizar una nueva operacion o salir de la calculadora?")
        exxit = input("\n\nElija 'NUEVA' o 'SALIR': ").lower()
        if exxit == "salir" :
            exit = True
        elif exxit == "nueva" :
            exxit = False
            os.system('cls')
        else :
            print("¡Opcion no valida, cerrando el sistema!")

    elif op == "multiplicacion" :
        num3 = num1*num2
        print(f"\n\tEste es el resultado: {num3: .2f}")
        print("\n\n\t¿Quieres realizar una nueva operacion o salir de la calculadora?")
        exxit = input("\n\nElija 'NUEVA' o 'SALIR': ").lower()
        if exxit == "salir" :
            exit = True
        elif exxit == "nueva" :
            exxit = False
            os.system('cls')
        else :
            print("¡Opcion no valida, cerrando el sistema!")

    elif op == "division" :
        num3 = num1/num2
        print(f"\n\tEste es el resultado: {num3: .2f}")
        print("\n\n\t¿Quieres realizar una nueva operacion o salir de la calculadora?")
        exxit = input("\n\nElija 'NUEVA' o 'SALIR': ").lower()
        if exxit == "salir" :
            exit = True
        elif exxit == "nueva" :
            exxit = False
            os.system('cls')
        else :
            print("¡Opcion no valida, cerrando el sistema!")
       
    else :
        print(f"{op} no es una operacion disponible")
        os.system('cls')

os.system('cls')
print("\n\t ¡Operacion finalizada!\n\n")