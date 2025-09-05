print("Una fuerte luz invade tu habitacion en la mitad de la noche, una fuerza mueve tu cuerpo a traves del edificio en el que vives, tu cuerpo se vuelve intangible y es transportado a traves de un rayo de luz a una gigantesca nave espacial. Al llegar al final del rayo de luz una luz blanca te ciega y te encuentras atrapado en una camilla de metal, un grupo de aliens estan hablando en un idioma que no entiendes y dejan la habitacion un tiempo luego.")
option1 = input("\n\tQue haras? ESCAPAR o ESPERAR: ").lower()
if option1 == "escapar" :
    print("\n\nConsigues aflojar las cintas que te atrapan y liberarte de la camilla, la puerta por la que los aliens salieron esta abierta y tiene dos pasillos.")
    option1_1 = input("\n\tPor cual pasillo iras? IZQUIERDO o DERECHO: ").lower()
    if option1_1 == "izquierdo" :
        print("Entras a una habitacion extensas, dos puertas grandes se alzan ante ti, una lleva a los motores de la nave, la otra a armeria")
        option1_1_1 = input("Por cual puerta iras? MOTORES o ARMERIA").lower()
        if option1_1_1 == "motores" :
            print("Encuentras dos herramientas extrañas en el suelo, una parece ser un tubo de algun tipo de metal con varias puntas diferentes y un circulo hecho de algo viscoso y que parece corrosivo.")
            option1_1_1_1 = input("Cual herramienta elegiras? TUBO o CIRCULO").lower()
            if option1_1_1_1 == "tubo" :
                print("Tomaste el tubo y tienes dos opciones, tratar de destruir los motores o intentar luchar con los alienigenas")
                option1_1_1_1_1 = input("Que haras? DESTRUIR o LUCHAR").lower()
                if option1_1_1_1_1 == "destruir" :
                    print("Insertas el tubo en los motores de la nave y ves como se detienen, escuchas explosiones en la distancia, parece que dañaste fatalmente la nave.")
                    option1_1_1_1_1_1 = input("Que haras? HUIR o QUEDARTE").lower()
                    if option1_1_1_1_1_1 == "huir" :
                        print("Sales al pasillo, encontrando un objeto que te teletransporta a la superficie, ves la nave caer a la distancia.")
                    elif option1_1_1_1_1_1 == "quedarte" :
                        print("La nave explota desde adentro, los motores fallan y se estrella en la tierra, tu y todos los aliens mueren en el impacto.")
                    else :
                        print("La nave se estabiliza despues de un tiempo y un grupo de guardias aliens te encuentran. Eres terminado en el instante.")
                elif option1_1_1_1_1 == "luchar" :
                    print("Sales corriendo al pasillo fuera de la zona de motores, un grupo de cientificos aliens desarmados se ven al final del pasillo, un grupo de guardias del otro lado.")
                    option1_1_1_1_1_2 = input("Que aliens atacaras? CIENTIFICOS o GUARDIAS").lower()
                    if option1_1_1_1_1_2 == "cientificos" :
                        print("Atacas a los aliens desarmados, tomando el dispositivo de escape que intentaban utilizar, eres transportado a la tierra en un pais lejano al tuyo.")
                    elif option1_1_1_1_1_2 == "guardias" :
                        print("Intentas luchar contra los guardias, pero no eres rival para ellos, te detienen justo antes de que la nave se estrelle.")
                    else :
                        print("Tardas demasiado en decidir, una torreta de la nave te derriba antes de que puedas hacer algo.")
            elif option1_1_1_1 == "circulo" :
                print("Tomaste el circulo, el mango evita que tu mano se derrita por el material viscoso. Puedes intentar derretir los motores o la pared de la nave.")
                option1_1_1_1_2 = input("Que derretiras? MOTORES o PARED").lower()
                if option1_1_1_1_2 == "motores" :
                    print("Derrites los motores, los cuales")
                    option1_1_1_1_2_2 = input("Que haras? HUIR o QUEDARTE").lower()
                    if option1_1_1_1_2_2 == "huir" :
                        print("Sales al pasillo, encontrando un objeto que te teletransporta a la superficie, ves la nave caer a la distancia.")
                    elif option1_1_1_1_2_2 == "quedarte" :
                        print("La nave explota desde adentro, los motores fallan y se estrella en la tierra, tu y todos los aliens mueren en el impacto.")
                    else :
                        print("La nave se estabiliza despues de un tiempo y un grupo de guardias aliens te encuentran. Eres terminado en el instante.")
                elif option1_1_1_1_2 == "pared" :
                    print("Sales corriendo al pasillo fuera de la zona de motores, un grupo de cientificos aliens desarmados se ven al final del pasillo, un grupo de guardias del otro lado.")
                    option1_1_1_1_1_2 = input("Que aliens atacaras? CIENTIFICOS o GUARDIAS").lower()
                    if option1_1_1_1_1_2 == "cientificos" :
                        print("Atacas a los aliens desarmados, tomando el dispositivo de escape que intentaban utilizar, eres transportado a la tierra en un pais lejano al tuyo.")
                    elif option1_1_1_1_1_2 == "guardias" :
                        print("Intentas luchar contra los guardias, pero no eres rival para ellos, te detienen justo antes de que la nave se estrelle.")
                    else :
                        print("Tardas demasiado en decidir, una torreta de la nave te derriba antes de que puedas hacer algo.")

    elif option1_1 == "derecho" :
elif option1 == "esperar" :
    print()