import os
import time
import random
os.system('cls')

#title = ["E", "X", "A", "M", "E", "N"]
print("\n\n\t\t\t\t", end="")
#for title1 in title:
#    print(" ", title1, end="", flush=True)
#    time.sleep(0.2)
exit = False
while exit == False:
    menu = int(input("\n\n\tIngrese el numero de ejercicio que quiere ver: "))
    if menu == 1:
        print("\n\n\tEJERCICIO 1")
        data = int(input("Ingrese el valor de su compra: "))
        data *= 1.15
        print(f"\n\nEl total de su compra es de {data} incluyendo un 15% de propina")

    elif menu == 2:
        print("\n\n\tEJERCICIO 2")
        temp1 = int(input("Ingrese la temperatura en grados celcius: "))
        temp2 = (temp1 * 9/5) + 32
        print(f"\n\nLa temperatura ingresada en celcius es {temp2} en farenthait.")

    elif menu == 3:
        print("\n\n\tEJERCICIO 3")
        num = int(input("Ingrese un numero, el programa decifrara si es positivo, negativo o cero: "))
        if num < 0:
           print("\n\nEl numero es negativo.")
        elif num > 0:
            print("\n\nEl numero es positivo.")
        else:
            print("\n\nEl numero es cero.")
    
    elif menu == 4:
        print("\n\n\tEJERCICIO 4")
        for i1 in range(51):
            e = i1 % 5
            if e == 0:
                print("", i1, end="", flush=True)

    elif menu == 5:
        print("\n\n\tEJERCICIO 5")
        lista_compras = []
        for i3 in range(5):
            a = input("Añadir articulos: ")
            lista_compras.append(a)
            print(lista_compras)
        del lista_compras[2]
        print(lista_compras)
            
    elif menu == 6:
        print("\n\n\tEJERCICIO 6")
        word = input("Ingrese una plabra: ")
        iword = word[::-1]
        print(iword)

    elif menu == 7:
        print("\n\n\tEJERCICIO 7")
        table = int(input("Ingrese un numero, el programa le dara su tabla de multiplicar: "))
        ftable = table
        for i2 in range(11):
            if i2 > 0:
                btable = table * i2
                print(f"{ftable} x {i2} = {btable}")

    elif menu == 8:
        print("\n\n\tEJERCICIO 8")
        snum = random.randint(1, 10)
        snumexit = False
        
        while snumexit == False:
            snumselect = int(input("El programa tiene un numero seleccionado, intente adivinarlo: "))
            if snumselect < snum:
                print("\nEl numero que ingreso es menor que el numero secreto.\n")
                input()
                os.system('cls')
            elif snumselect > snum:
                print("\nEl numero que ingreso es mayor que el numero secreto.\n")
                input()
                os.system('cls')
            else:
                snumexit = True
                print("\nEl numero que ingreso es el numero secreto.\n")
                input()
                os.system('cls')
    
    elif menu == 9:
        print("\n\n\tEJERCICIO 9")
        pswlenexit = False
        while pswlenexit == False:
            pswlen = input("Ingrese su contraseña: ")
            if len(pswlen) < 8:
                print("Tu contraseña es muy corta, debe tener al menos 8 caracteres.")
            else:
                print("Tu contraseña es valida.")
                pswlenexit = True
    
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
        print(f"Diccionario final: {dic1}")
    
    elif menu == 11:
        print("\n\n\tEJERCICIO 11")
        rlist = ["a", "b", "c", "d", "e", "d", "e", "a"]
        print(f"Lista original: {rlist}")
        rset = set(rlist)
        print(rset)
    
    elif menu == 12:
        print("\n\n\tEJERCICIO 12")
        numero = int(input("agrege un numero"))
        ex = int(input("agrege un numero"))
        ognum = numero
        for i in range(ex):
            numero=numero*ognum
            print(numero)

    elif menu == 13:
        print("\n\n\tEJERCICIO 13")
        poslist = ["1","2","3","4","5","6","7","8","9","10"]
        print(poslist)
        inlist = input("Elija un elemento de la lista, el programa le dira su posicion: ")
        if inlist in poslist:
            numlist = poslist.index(inlist)
            print(f"La posicion de ese elemento en la lista es: {numlist}")
    
    elif menu == 14:
        print("\n\n\tEJERCICIO 14")
        mi_diccionario= {
        "nombre": "",
        "apellido": "",
        "edad":0,
        }
        edad1 = int(input("ingrese su edad: "))
        mi_diccionario["edad"] = edad1
        nombre1 = (input("ingrese su nombre: "))
        mi_diccionario["nombre"]= nombre1
        apellido1 = (input("ingrese su apellido: "))
        mi_diccionario["apellido"]= apellido1

        for clave, valor in mi_diccionario.items():
            print(f"{clave}: {valor}")

    elif menu == 15:
        print("\n\n\tEJERCICIO 15")

    elif menu == 21:
        print("\n\n\tEJERCICIO 21: FINAL")
        alm = [
               ("Juan", "Matematicas", 35, 8),
               ("Pedro", "Matematicas", 90, 5),
               ("Alberto", "Matematicas", 100, 10)
               ("Manuel", "Matematicas", 30, 4)
               ("Antonio", "Matematicas", 80, 8)
              ]