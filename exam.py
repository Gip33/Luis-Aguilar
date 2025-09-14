import os
import time
import random
os.system('cls')

#title = ["E", "X", "A", "M", "E", "N"]
#print("\n\n\t\t\t\t", end="")
#for title1 in title:
#    print(" ", title1, end="", flush=True)
#    time.sleep(0.2)
exit = False
while exit == False:
    print("1. Calculadora de Propinas 💵")
    print("2. Conversor de Temperatura 🌡")
    print("3. Clasificador de Números ➕➖")
    print("4. Múltiplos de 5 🖐")
    print("5. Gestor de Lista de Compras 🛒")
    print("6. Inversor de Cadenas 🔄")
    print("7. Tabla de Multiplicar 🔢")
    print("8. Adivina el Número 🎯")
    print("9. Validador de Contraseña Simple 🔐")
    print("10. Combinador de Diccionarios 🧩")
    print("11. Eliminación de Duplicados 🧬")
    print("12. Calculadora de Potencia ⚡")
    print("13. Encontrar el Índice 📍")
    print("14. Diccionario de Información Personal 👤")
    print("15. Suma de una Matriz 🧮")
    print("16. Validación de Entrada en Bucle 🛡")
    print("17. Encontrar el Máximo sin max() 🏔")
    print("18. Palabra más Larga 📏")
    print("19. Contador de Mayúsculas y Minúsculas Aa")
    print("20. Registro de Gastos Simple 🧾")
    print("21. Procesador de Calificaciones Academicas 📠")
    menu = int(input("\n\n\tIngrese el numero de ejercicio que quiere ver: "))
    os.system('cls')

    if menu == 1:
        print("\n\n\tEJERCICIO 1")
        data = float(input("Ingrese el valor de su compra: "))
        tip = data * 0.15
        total = data + tip
        print(f"\n\nEl total de su compra es de {total} incluyendo un 15% de propina")
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')

    elif menu == 2:
        print("\n\n\tEJERCICIO 2")
        temp1 = int(input("Ingrese la temperatura en grados celcius: "))
        temp2 = (temp1 * 9/5) + 32
        print(f"\n\nLa temperatura ingresada en celcius es {temp2} en farenthait.")
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')

    elif menu == 3:
        print("\n\n\tEJERCICIO 3")
        num = int(input("Ingrese un numero, el programa decifrara si es positivo, negativo o cero: "))
        if num < 0:
           print("\n\nEl numero es negativo.")
        elif num > 0:
            print("\n\nEl numero es positivo.")
        else:
            print("\n\nEl numero es cero.")
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')
    
    elif menu == 4:
        print("\n\n\tEJERCICIO 4")
        print("Multiplos de 5 hasta el 50: \t")
        for i1 in range(51):
            e = i1 % 5
            if e == 0:
                print("", i1, end="", flush=True)
        print("\n\n")
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')

    elif menu == 5:
        print("\n\n\tEJERCICIO 5")
        print("Ingrese 5 articulos, el segundo que ingrese sera eliminado de la lista.\n")
        lista_compras = []
        for i3 in range(5):
            a = input("Añadir articulos: ")
            lista_compras.append(a)
            print(f"Su lista tiene: {lista_compras}")
        del lista_compras[1]
        print(f"Su lista final con el segundo articulo eliminado es: {lista_compras}")
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')
            
    elif menu == 6:
        print("\n\n\tEJERCICIO 6")
        word = input("Ingrese una plabra: ")
        iword = word[::-1]
        print(f"{word} al reves es: {iword}")
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')

    elif menu == 7:
        print("\n\n\tEJERCICIO 7")
        table = int(input("Ingrese un numero, el programa le dara su tabla de multiplicar: "))
        ftable = table
        for i2 in range(11):
            if i2 > 0:
                btable = table * i2
                print(f"{ftable} x {i2} = {btable}")
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')

    elif menu == 8:
        print("\n\n\tEJERCICIO 8")
        snum = random.randint(1, 20)
        snumexit = False
        
        while snumexit == False:
            snumselect = int(input("El programa tiene un numero seleccionado, intente adivinarlo: "))
            if snumselect < snum:
                print("\nEl numero que ingreso es menor que el numero secreto.\n")
                
            elif snumselect > snum:
                print("\nEl numero que ingreso es mayor que el numero secreto.\n")
                
            else:
                snumexit = True
                print("\nEl numero que ingreso es el numero secreto.\n")
                
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')
    
    elif menu == 9:
        print("\n\n\tEJERCICIO 9")
        pswlenexit = False
        while pswlenexit == False:
            pswlen = input("Ingrese su contraseña: ")
            if len(pswlen) < 8:
                print("Tu contraseña es muy corta, debe tener al menos 8 caracteres.\n")
            else:
                print("Tu contraseña es valida.\n")
                pswlenexit = True
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')
    
    elif menu == 10:
        print("\n\n\tEJERCICIO 10")
        dic1 = {
            "Color1": "rojo",
            "Animal1": "perro"
        }
        dic2 = {
            "Color2": "negro",
            "Animal2": "gato"
        }
        print(f"Diccionario 1: {dic1}")
        print(f"Diccionario 2: {dic2}")
        dic1.update(dic2)
        print(f"Diccionario final: {dic1}\n")
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')
    
    elif menu == 11:
        print("\n\n\tEJERCICIO 11")
        rlist = ["a", "b", "c", "d", "e", "d", "e", "a"]
        print(f"Lista original: {rlist}")
        rset = set(rlist)
        print(f"Lista con los contenidos duplicados removidos: {rset}\n")
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')
    
    elif menu == 12:
        print("\n\n\tEJERCICIO 12")
        numero = int(input("Agrege un numero: "))
        ex = int(input("Agrege un exponente: "))
        ognum = numero
        print(ognum)
        for i in range(ex-1):
            numero=numero*ognum
            print(numero)
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')

    elif menu == 13:
        print("\n\n\tEJERCICIO 13")
        poslist = ["1","2","3","4","5","6","7","8","9","10"]
        print(poslist)
        inlist = input("Elija un elemento de la lista, el programa le dira su posicion: ")
        if inlist in poslist:
            numlist = poslist.index(inlist)
            print(f"La posicion de ese elemento en la lista es: {numlist}")
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')
    
    elif menu == 14:
        print("\n\n\tEJERCICIO 14")
        mi_diccionario= {
        "Nombre": "",
        "Apellido": "",
        "Edad":0,
        }
        edad1 = int(input("Ingrese su edad: "))
        mi_diccionario["Edad"] = edad1
        nombre1 = (input("Ingrese su nombre: "))
        mi_diccionario["Nombre"]= nombre1
        apellido1 = (input("Ingrese su apellido: "))
        mi_diccionario["Apellido"]= apellido1
        print("")

        for clave, valor in mi_diccionario.items():
            print(f"{clave}: {valor}")
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')

    elif menu == 15:
        print("\n\n\tEJERCICIO 15")

    elif menu == 16:
        print("\n\n\tEJERCICIO 16")
        while True:
            validnum = int(input("Ingrese un numero del 1 al 10: "))
            if validnum > 10 or validnum < 1:
                print("El numero que ingreso no es valido.")
            else:
                break
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')
    
    elif menu == 17:
        print("\n\n\tEJERCICIO 17")
        print("Ingrese 10 numeros uno a uno, el programa creara una lista y resaltara el mayor de ellos.")
        maxlist = []
        for i4 in range(10):
            maxlistnum = int(input("Ingrese un numero: "))
            maxlist.append(maxlistnum)
        for i5 in maxlist:
            maxnum = 0
            if i5 > maxnum:
                maxnum = i5
        print(f"El numero mas grande de la lista es: {maxnum}")
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')
    
    elif menu == 18:
        print("\n\n\tEJERCICIO 18")
        phrase = input("Escriba una frase: ")
        phraselist = phrase.split()
        lenght = 0
        for i7 in phraselist:
            if len(i7) > lenght:
                lword = i7
                lenght=len(i7)
        print(f"La palabra mas larga de esa frase es: {lword} y tiene {lenght} letras.")
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')

    elif menu == 19:
        print("\n\n\tEJERCICIO 19")
        text = input("Escriba un texto: ")
        upper_count = 0
        lower_count = 0

        for char in text:
            if char.isupper():
                upper_count += 1
            elif char.islower():
                lower_count += 1

        print(f"Mayúsculas: {upper_count}")
        print(f"Minúsculas: {lower_count}")
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')
    
    elif menu == 20:
        print("\n\n\tEJERCICIO 20")
        print("Escriba 'SALIR' en vez del nombre del gasto para detener la lista.")
        expenses = {}
        while True:
            key = input("\nIngrese el nombre del gasto: ").lower()
            if key == "salir":
                break
            value = float(input(f"Ingrese el valor para '{key}': "))
            expenses[key] = value
        fvalue = 0
        print("Su lista es: ")
        for key, value in expenses.items():
            
            print(f"GASTO: {key}\tVALOR: ${value}")
            fvalue += value
        print(f"Su total es de ${fvalue}.")
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')

    elif menu == 21:
        print("\n\n\tEJERCICIO 21: FINAL")
        alm = [
               ("Juan", "Matematicas", 35, 8),
               ("Pedro", "Matematicas", 90, 5),
               ("Alberto", "Matematicas", 100, 10),
               ("Manuel", "Matematicas", 30, 4),
               ("Antonio", "Matematicas", 80, 8)
              ]
        
        aproved = []
        failed = []
        honor = []
        
        for i6 in alm:
            note = i6[2]
            assist = i6[3]
            print(f"ESTUDIANTE: {i6[0]}\nMATERIA: {i6[1]}\nNOTA: {i6[2]}\nASISTENCIAS: {i6[3]}\n\n")
            if assist < 8:
                failed.append(i6[0])
            if note < 70 and i6[0] not in failed:
                failed.append(i6[0])
            elif note >= 70 and i6[0] not in failed:
                aproved.append(i6[0])
            if note >= 95 and assist >= 9:
                honor.append(i6[0])
        
        print(f"Estudiantes aprobados: {aproved}")
        print(f"Estudiantes reprobados: {failed}")
        print(f"Estudiantes en el cuadro de honor: {honor}")
        input("Precione ENTER para salir a la pantalla de seleccion: ")
        os.system('cls')

