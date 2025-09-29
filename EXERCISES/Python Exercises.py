import os
import random
os.system('cls')

def tips():
    print("Registro de pago:\n")
    value = int(input("Digite el costo total de su cuenta: "))
    tip = int(input("Digite el porcentaje de propina que desea dar: "))

    tip = (tip/100)+1
    fvalue = value*tip
    print(f"\nEste es el valor total de su cuenta despues de la propina: {fvalue}")

    input("\n\nDigite 'ENTER' para volver al menu.")
    os.system('cls')
    menu()

def vote():
    print("Proceso de votacion:\n")
    voteage = int(input("Ingrese su edad: "))
    
    if voteage >= 18:
        print("\nTienes la edad necesaria para votar.")
    else:
        print("\nNo tienes la edad necesaria para votar.")
    
    input("\n\nDigite 'ENTER' para volver al menu.")
    os.system('cls')
    menu()

def odsum():
    print("Suma de numeros pares:\n")
    odtop = int(input("Digite el numero maximo al que el programa contara: "))
    fvalue = 0

    for i in range(odtop+1):
        odvalue = i % 2
        if odvalue == 0:
            fvalue += i
    print(f"El valor final al sumar todos los pares es: {fvalue}")

    input("\n\nDigite 'ENTER' para volver al menu.")
    os.system('cls')
    menu()
    
def secretnum():
    print("Adivina el numero secreto:\n")
    print("El programa genero un numero del 1 al 50")
    randnum = random.randint(1,50)
    print(randnum)
    while not False:
        ptry = int(input("\n\tAdivine el numero: "))
        if ptry < randnum:
            print("\tEl numero que digito es menor que el numero secreto.")
        elif ptry > randnum:
            print("\tEl numero que digito es mayor que el numero secreto.")
        else:
            print("\tEl numero que digito es el numero secreto!")
            break
    
    input("\n\nDigite 'ENTER' para volver al menu.")
    os.system('cls')
    menu()

def vowels():
    print("Contador de Vocales:\n")
    text = input("Ingrese una frase: ")
    allvowels = "aeiouAEIOU"
    vowelcount = 0

    for e in text:
        if e in allvowels :
            vowelcount += 1
    print(f"Lo que escribio tiene {vowelcount} vocales.")

    input("\n\nDigite 'ENTER' para volver al menu.")
    os.system('cls')
    menu()

def menu():
    while not False:
        print("Python Exercises\n\n")
        print("\t1. Calculadora de propinas.")
        print("\t2. Edad pra votar.")
        print("\t3. Suma de numeros pares.")
        print("\t4. Adivina el numero secreto.")
        print("\t5. Contador de vocales.")
        menu = int(input("\nElige un ejercicio: "))

        os.system('cls')
        if menu == 1:
            tips()
        elif menu == 2:
            vote()
        elif menu == 3:
            odsum()
        elif menu == 4:
            secretnum()
        elif menu == 5:
            vowels()
        else:
            print("El numero que eligio no corresponde a ningun ejercicio.")
            input("\n\nDigite 'ENTER' para volver al menu.")
            os.system('cls')
    

menu()