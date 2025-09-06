import os
os.system('cls')

print("\n\n\t\tBIENVENIDO VOTANTE")
print("\nPara participar en la votacion es requerida su edad y un registro valido en el CNE")
age = int(input("\n\n\tIngrese su edad: "))
cne = input("\n\n\t¿Tiene usted una cuenta en el CNE? (SI/NO): ").lower()

if age>=18 and cne == "si":
    print("\n\n¡Acceso concedido, prosiga para realizar su voto!")
else :
    print("\n\nSus datos no son validos para votar :p")

