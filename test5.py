import os
import time

os.system('cls')

title = ["T", "I", "T", "U", "L", "O"]

print("\n\n")
for title1 in title:
    print(" ", title1, end="", flush=True)
    time.sleep(0.1)

num = 1
print("\n\nBUCLE WHILE\n\n")
while num <= 10:
    print(num, end=" ", flush=True)
    num += 1
    time.sleep(0.1)

print("\n\nBUCLE FOR\n\n")
for num2 in range(10):
    num2 += 1
    print(num2, end=" ", flush=True)
    time.sleep(0.1)

dictionary = {
    "Nombre": "Luis",
    "Edad": 17,
    "Apellido": "Aguilar",
    "Color favorito": "Rojo",
    "Animal favorito": "Cocodrilo"
}
print("\n\nDICCIONARIO\n\n")
for key,value in dictionary.items():
    print(f"{key}:", end=" ", flush=True)
    time.sleep(0.25)
    print(f"{value}.")
    time.sleep(0.25)

input("\n\n")