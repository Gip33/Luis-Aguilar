import os
os.system("cls")
win = False

print("\n\nUna fuerte luz invade tu habitacion en la mitad de la noche, una fuerza mueve tu cuerpo a traves del edificio en el que vives, tu cuerpo se vuelve intangible y es transportado a traves de un rayo de luz a una gigantesca nave espacial. Al llegar al final del rayo de luz una luz blanca te ciega y te encuentras atrapado en una camilla de metal, un grupo de aliens estan hablando en un idioma que no entiendes y dejan la habitacion un tiempo despues.")
option1 = input("\n\tQue haras? ESCAPAR o ESPERAR: ").lower()

if option1 == "escapar" :
    print("\n\nConsigues aflojar las cintas que te atrapan y liberarte de la camilla, la puerta por la que los aliens salieron esta abierta y tiene dos pasillos.")
    option1_1 = input("\n\tPor cual pasillo iras? IZQUIERDO o DERECHO: ").lower()

    if option1_1 == "izquierdo" :
        print("\n\nEntras a una habitacion extensas, dos puertas grandes se alzan ante ti, una lleva a los motores de la nave, la otra a armeria")
        option1_1_1 = input("\n\tPor cual puerta iras? MOTORES o ARMERIA: ").lower()

        if option1_1_1 == "motores" :
            print("\n\nEncuentras dos herramientas extrañas en el suelo, una parece ser un tubo de algun tipo de metal con varias puntas diferentes y un circulo hecho de algo viscoso y que parece corrosivo.")
            option1_1_1_1 = input("\n\tCual herramienta elegiras? TUBO o CIRCULO: ").lower()

            if option1_1_1_1 == "tubo" :
                print("\n\nTomaste el tubo y tienes dos opciones, tratar de destruir los motores o intentar luchar con los alienigenas")
                option1_1_1_1_1 = input("\n\tQue haras? DESTRUIR o LUCHAR: ").lower()

                if option1_1_1_1_1 == "destruir" :
                    print("\n\nInsertas el tubo en los motores de la nave y ves como se detienen, escuchas explosiones en la distancia, parece que dañaste fatalmente la nave.")
                    option1_1_1_1_1_1 = input("\n\tQue haras? HUIR o QUEDARTE: ").lower()

                    if option1_1_1_1_1_1 == "huir" :
                        print("\n\nSales al pasillo, encontrando un objeto que te teletransporta a la superficie, ves la nave caer a la distancia.")
                        win = True
                    elif option1_1_1_1_1_1 == "quedarte" :
                        print("\n\nLa nave explota desde adentro, los motores fallan y se estrella en la tierra, tu y todos los aliens mueren en el impacto.")
                        win = False
                    else :
                        print("\n\nLa nave se estabiliza despues de un tiempo y un grupo de guardias aliens te encuentran. Eres terminado en el instante.")
                        win = False

                elif option1_1_1_1_1 == "luchar" :
                    print("\n\nSales corriendo al pasillo fuera de la zona de motores, un grupo de cientificos aliens desarmados se ven al final del pasillo, un grupo de guardias del otro lado.")
                    option1_1_1_1_1_2 = input("\n\tQue aliens atacaras? CIENTIFICOS o GUARDIAS").lower()

                    if option1_1_1_1_1_2 == "cientificos" :
                        print("\n\nAtacas a los aliens desarmados, tomando el dispositivo de escape que intentaban utilizar, eres transportado a la tierra en un pais lejano al tuyo.")
                        win = True
                    elif option1_1_1_1_1_2 == "guardias" :
                        print("\n\nIntentas luchar contra los guardias, pero no eres rival para ellos, te detienen justo antes de que la nave se estrelle.")
                        win = False
                    else :
                        print("\n\nTardas demasiado en decidir, una torreta de la nave te derriba antes de que puedas hacer algo.")
                        win = False
                else :
                    print("\n\nNo tomas ninguna accion, los guardias aliens te encuentran y te terminan.")
                    win = False

            elif option1_1_1_1 == "circulo" :
                print("\n\nTomaste el circulo, el mango evita que tu mano se derrita por el material viscoso. Puedes intentar derretir los motores, el suelo o la pared de la nave.")
                option1_1_1_1_2 = input("\n\tQue derretiras? PARED, SUELO o MOTORES: ").lower()

                if option1_1_1_1_2 == "motores" :
                    print("\n\nIntentas derretir los motores, los cuales se detienen por un momento antes de resumir su actividad, parece que el acido no es lo suficientemente efectivo contra lo motores, pero quizas puedas derretir la pared y huir. La nave ha ascendido a la alta atmosfera")
                    option1_1_1_1_2_2 = input("\n\tQue derretiras? MOTORES o PARED: ").lower()

                    if option1_1_1_1_2_2 == "motores" :
                        print("\n\nIntentas derretir los motores de nuevo, pero no funciona. La nave se mantiene en funcionamiento y escuchas los pasos de los guardias acercandose a ti.")
                        win = False
                    elif option1_1_1_1_2_2 == "pared" :
                        print("\n\nDerrites la pared de la nave, siendo lanzado a la alta atmosfera, muriendo en el instante.")
                        win = False
                    else :
                        print("\n\nEl acido de tu herramienta lentamente empieza a corroer tu mano, muriendo en el proceso.")
                        win = False

                elif option1_1_1_1_2 == "pared" :
                    print("\n\nDerrites la pared de la nave. No pareces estar tan lejos de la superficie, y mientras la pared se derrite tienes tiempo para pensar en como escapar.")
                    option1_1_1_1_1_2 = input("\n\tQue haras? ESPERAR o BUSCAR: ").lower()

                    if option1_1_1_1_1_2 == "esperar" :
                        print("\n\nDecides esperar a que la pared se derrita por completo, saltando desde la nave. Mueres en el impacto contra la tierra.")
                        win = False
                    elif option1_1_1_1_1_2 == "buscar" :
                        print("\n\nDecides buscar una algo que te ayude a sobrevivir la caida, encuentras un dispositivo que crea un campo de energia, permitiendote caer desde la nave hasta la tierra sin sufrir daño.")
                        win = True
                    else :
                        print("\n\nTardas demasiado en decidir, el acido de tu herramienta lentamente empieza a corroer tu mano, muriendo en el proceso.")
                        win = False
                
                elif option1_1_1_1 == "suelo" :
                    print("\n\nUtilizas el acido para derretir el suelo, creando un agujero por el que puedes caer, una habitacion aparentemente vacia se encuentra bajo a ti.")
                    option1_1_1_1_3_2 = input("\n\tQue haras? CAER o ESPERAR: ").lower()

                    if option1_1_1_1_3_2 == "caer" :
                        print("\n\nCaes por el agujero, aterrizando en una habitacion vacia, puedes ver una señal que indica la presencia de capsulas de escape en el siguiente pasillo, las cuales usas para escapar.")
                        win = True
                    elif option1_1_1_1_3_2 == "esperar" :
                        print("\n\nDecides esperar a que los guardias te encuentren, los cuales te detienen antes de que puedas hacer algo.")
                        win = False

                else :
                    print("\n\nEl acido de tu herramienta lentamente empieza a corroer tu mano, muriendo en el proceso.")
                    win = False
            else :
                print("\n\n No tomas ninguna herramienta, los guardias aliens te encuentran y te terminan.") 
                win = False 
        
        elif option1_1_1 == "armeria" :
            print("\n\nEntras a la armeria y te encuentras con armas y objetos extraños que nunca has visto antes. Un baston de un metal extraño y un objeto esferico con una superficie oscura y reflejante llaman tu atencion.") 
            option1_1_3 = input("Que objeto tomaras?, BASTON o ESFERA: ").lower()

            if option1_1_3 == "baston" :
                print("\n\nTomas el baston, el cual tiene un brillo azulado y parece emitir una ligera vibracion. Escuchas pasos rapidos acercandose. Puedes intentar usarlo para defenderte o buscar una salida.")
                option1_1_3_1 = input("\n\tQue haras? DEFENDERTE o BUSCAR: ").lower()

                if option1_1_3_1 == "defenderte" :
                    print("\n\nTe preparas para defenderte, los guardias entran a la habitacion y te ven con el baston, uno de ellos intenta atacarte. El baston reacciona a la amenaza, una luz parpadea sobre un boton en el.")
                    option1_1_3_1_1 = input("\n\tQue haras? ATACAR o PRECIONAR BOTON: ").lower()

                    if option1_1_3_1_1 == "atacar" :
                        print("\n\nAtacas al guardia, el baston emite una descarga electrica que lo derriba, los otros guardias entran en alerta y te atacan, no eres rival para ellos y eres detenido.")
                        win = False
                    elif option1_1_3_1_1 == "precionar boton" :
                        print("\n\nPrecionas el boton, el baston emite una luz brillante que aturde a los guardias, aprovechando la oportunidad sales corriendo por el pasillo y encuentras una salida de emergencia, logras escapar de la nave y regresar a la tierra.")
                        win = True
                    else :
                        print("\n\nTardas demasiado en decidir y los guardias te encuentran y terminan contigo.")
                        win = False
                    
                elif option1_1_3_1 == "buscar" :
                    print("\n\nDecides buscar una salida, encontrando una puerta que lleva a una sala de control. En ella un grupo de aliens controlan una parte de la nave, los guardias entran en la sala tras de ti. Puedes intentar atacar a los aliens o esperar a los guardias.")
                    option1_1_3_1_1 = input("\n\tQue haras? ATACAR o ESPERAR: ").lower()

                    if option1_1_3_1_1 == "atacar" :
                        print("\n\nAtacas a los aliens indefensos, los cuales, temiendo por su vida, te apuntan a las capsulas de escape. Logras entrar a una y escapar de la nave, cayendo en un bosque lejano a tu casa.")
                        win = True
                    elif option1_1_3_1_1 == "esperar" :
                        print("\n\nDecides esperar a los guardias, los cuales te encuentran y te detienen antes de que puedas hacer algo.")
                        win = False
                    else :
                        print("\n\nNo eliges ninguna acción válida y los guardias te encuentran y terminan contigo.")
                        win = False
                else :
                    print("\n\nNo tomas ninguna acción válida y los guardias te encuentran y terminan contigo.")
                    win = False

            elif option1_1_3 == "esfera" :
                print("\n\nTomas la esfera, puedes sentir un boton bajo su superficie, si esta es un arma, quien sabe que pasara cuando aprietes el boton, puedes intentar presionar el boton ahora o esperar a presionarlo cuando entren los guardias.")
                option1_1_3_2 = input("\n\tQue haras? PRECIONAR o ESPERAR: ").lower()

                if option1_1_3_2 == "precionar" :
                    print("\n\nPresionas el boton, la esfera lanza dos rayos de luz a dos paredes de la armeria, los objetos detras de las paredes se hacen visibles, una pared conduce al exterior de la nave, la otra a una sala experimentacion.")
                    option1_1_3_2_1 = input("\n\tPor cual puerta iras? EXTERIOR o EXPERIMENTACION: ").lower()

                    if option1_1_3_2_1 == "exterior" :
                        print("\n\nSales por la puerta que lleva al exterior, cayendo en la alta atmosfera, muriendo en el proceso.")
                        win = False
                    elif option1_1_3_2_1 == "experimentacion" :
                        print("\n\nSales por la puerta que lleva a la sala de experimentacion. Puedes escuchar rujidos y gritos a lo lejos. Puntos brillantes se mueven en las oscuridad, son ojos, y antes de que puedas reaccionar, puedes sentir tu pecho siendo abierto por una garra.")
                        win = False
                    else :
                        print("\n\nTardas demasiado en decidir, los guardias te encuentran y terminan contigo. ")
                        win = False
                        
                elif option1_1_3_2 == "esperar" :
                    print("\n\nDecides esperar a los guardias, precionando el boton en el momento en el que entran, una explosion de luz los ciega temporalmente. Puedes precionar el boton de nuevo o intentar huir.")
                    option1_1_3_2_2 = input("\n\tQue haras? PRECIONAR o HUIR: ").lower()

                    if option1_1_3_2_2 == "precionar" :
                        print("\n\nPresionas el boton de nuevo, la esfera emite un rayo de luz que elimina a los guardias, aprovechando la oportunidad sales corriendo por el pasillo y encuentras una salida de emergencia, logras escapar de la nave y regresar a la tierra.")
                        win = True
                    elif option1_1_3_2_2 == "huir" :
                        print("\n\nIntentas huir, pero los guardias se recuperan y te alcanzan, terminandote antes de que puedas hacer algo.")
                        win = False
                    else :
                        print("\n\nTardas demasiado en decidir, los guardias se recuperan y terminan contigo.")
                        win = False

                else :
                    print("\n\nNo eliges ninguna acción, y los guardias entran a la sala y terminan contigo.")
                    win = False

            else :
                print("\n\nNo eliges ninguna acción, y los guardias entran a la sala y terminan contigo.")
                win = False

        else :
            print("\n\n No eliges ninguna puerta, y los guardias te encuentran y terminan contigo. ")
            win = False

    elif option1_1 == "derecho" :
        print("\n\nTe diriges por el pasillo derecho, al final del pasillo ves dos puertas grandes que se abren, llevandote a una enorme sala de control y a una habitacion llena de camillas con cadenas.") 
        option1_1_2 = input("\nPor cual puerta iras? CONTROL O CAMILLAS:").lower()

        if option1_1_2 == "control":
            print("\n\nEntras a la sala de control, varios aliens estan operando la nave, al verte entran en alerta y llaman a los guardias.")
            option1_1_2_2 = input("\n\nQue haras? HUIR o LUCHAR:").lower()

            if option1_1_2_2 == "huir":
                print("\n\nAl huir te encuestras con una puerta la cual lleva a un laboratorio vacio, exepto por otro humano que vez atado a una camilla, el cual te ve y te implora que lo ayudes.") 
                option1_1_2_2_2 = input("\n\nQue haras? AYUDARLO o SEGUIR HUYENDO:").lower()

                if option1_1_2_2_2 == "ayudarlo":
                    print(" \n\nLogras liberarlo y ambos salen corriendo por el pasillo, esta persona que te acompaña te guia a una sala donde hay capsulas de evacuacion.")
                    option1_1_2_2_2_1 = input("\n\nQue haras? ENTRAR o NO ENTRAR:").lower()

                    if option1_1_2_2_2_1 == "entrar":
                        print("\n\nLogran entrar a una capsula y escapar de la nave, cayendo en un bosque lejano a tu casa.") 
                        win = True
                    elif option1_1_2_2_2_1 == "no entrar":
                        print("\n\nDecides no confiar en el otro humano y seguir huyendo, pero los guardias te encuentran y terminan contigo. ") 
                        win = False
                    else:
                        print("\n\nTardas demasiado en decidir y los guardias te encuentran y terminan contigo. ") 
                        win = False

                elif option1_1_2_2_2 == "seguir huyendo": 
                    print("\n\nDecides huir e ignorar la suplicas de la otra persona y continuas por el pasillo. Encuentras una salida de emergencia y un hangar.")
                    option1_1_2_2_2_1 = input("\n\nQue camino seguiras? EMERGENCIA o HANGAR:").lower()

                    if option1_1_2_2_2_1 == "emergencia":
                        print("\n\nTe diriges a la salida de emergencia y logras escapar de la nave, cayendo en un bosque lejano a tu casa.")
                        win = True
                    elif option1_1_2_2_2_1 == "hangar":
                        print("\n\nTe diriges al hangar, pero al entrar puedes ver a otros aliens intentando abordar las naves, los guardias te atrapan y terminan contigo.")
                        win = False
                    else:
                        print("\n\nTardas demasiado en decidir y los guardias te encuentran y terminan contigo.")
                        win = False

                else:
                    print("\n\nTardas demasiado en decidir y los guardias te encuentran y terminan contigo.")
                    win = False

            elif option1_1_2_2 == "luchar": 
                print("\n\nIntentas luchar contra los navegantes para tomar control de la nave, uno de ellos corre hacia un boton de alerta, puedes atacarlo o intentar tomar control de la nave.") 
                option1_1_2_2 = input("\n\nQue haras? ATACARLO o TOMAR CONTROL: ").lower()

                if option1_1_2_2 == "atacarlo":
                    print("\n\nAtacas al alien y lo derribas, evitando que llame a los guardias. Los otros aliens toman control de la nave nuevamente, puedes intentar quitarle el control de la nave a los aliens o pulsar uno de los botones de la consola que tienes enfrente.")
                    option1_1_2_2_1 = input("\n\nQue haras? QUITAR CONTROL o PULSAR BOTON: ").lower()

                    if option1_1_2_2_1 == "quitar control":
                        print("\n\nIntentas quitarle el control de la nave a los aliens, pero no tienes idea de como hacerlo, estrellando la nave contra la tierra.") 
                        win = False
                    elif option1_1_2_2_1 == "pulsar boton":
                        print("\n\nDecides pulsar uno de los botones de la consola, desestabilizando la nave y causando que se desplace fuera de control. Estrellas la nave contra la tierra.")
                        win = False
                    else:
                        print("\n\nTardas demasiado en decidir y los guardias te encuentran y terminan contigo. ") 
                        win = False

                elif option1_1_2_2 == "tomar control": 
                    print("\n\nCorres hacia la consola, quitando a los aliens del camino y tomando control de la nave, puedes intentar regresar a la tierra o estrellar la nave en algun lugar alejado.")
                    option1_1_2_2_1 = input("\n\nQue haras? REGRESAR a la tierra o ESTRELLAR la nave: ").lower()

                    if option1_1_2_2_1 == "estrellar":
                        print("\n\nDecides estrellar la nave en un lugar alejado, alejandote de la civilizacion y asegurandote de que nadie mas sufra a manos de los aliens. ") 
                        win = True
                    elif option1_1_2_2_1 == "regresar":
                        print("\n\nDecides regresar a la tierra, pero no sabes como pilotear la nave y terminas estrellandote en el oceano, muriendo en el proceso. ") 
                        win = False
                    else:
                        print("\n\nTardas demasiado en decidir y los guardias te encuentran y terminan contigo. ") 
                        win = False
                
                else:
                    print("\n\nTardas demasiado en decidir y los guardias te encuentran y terminan contigo. ") 
                    win = False

            else:
                print("\n\nTardas demasiado en decidir y los guardias te encuentran y terminan contigo. ") 
                win = False
    
        elif option1_1_2 == "camillas": 
            print("\n\nEntras a la habitacion llena de camillas, varias de ellas tienen humanos atados, puedes intentar liberarlos o buscar algun objeto que te ayude a escapar.") 
            option2 = input("que haras?, LIBERARLOS O BUSCAR: ") 

            if option2 == "liberarlos" : 
                print("Optas por liberar a los humanos atados, uno de ellos dice haber sido transportado por las intalaciones cuando experimentaron con el y recuerda ciertos caminos en la nave, ofrece guiarte al hangar para escapar, los otros humanos no parecen confiar en el y escapan por el sistema de ventilacion.") 
                option2_2 = input("¿Qué plan eliges?, VENTILACION O HANGAR") 

                if option2_2 == "ventilacion" : 
                    print("Decides ignorar al guía y seguir por el conducto de ventilación, los otros humanos y tu avanzan hasta llegar a una interseccion, tu, como su liberador, eres seleccionado para elegir.")
                    option2_2_2 = input("que elejiras? IZQUIERDA O DERECHA: ") 

                    if option2_2_2 == "izquierda" :
                        print("Eliges el camino de la izquierda. Mientras mas avanzan, un calor insoportable empieza a emanar de las paredes del conducto. El aire se vuelve denso y difícil de respirar. Al llegar a una rejilla puedes ver que estan sobre los motores, pero es demasiado tarde para hacer algo, el calor intenso y la falta de oxigeno hacen que tu y los otros humanos caigan inconscientes.")
                        win = False 
                    elif option2_2_2 == "derecha" : 
                        print("Eliges el camino de la derecha. El conducto se vuelve mas frio y facil de respirar, al llegar a una rejilla puedes ver que estan sobre una salida de emergencia, logran salir de la nave y regresar a la tierra.") 
                        win = True
                    else : 
                        print("tardas en tomar una decision y los guardias te atrapan")
                        win = False
            
                elif option2_2 == "hangar" : 
                    print("Decides seguir al guia, dejando a los demas humanos atras y dirigiendote al hangar, al llegar te preguntas a ti mismo si entrar a la puerta o buscar otra salia")
                    option2_2_2 = input("que haras? ENTRAR o BUSCAR: ")

                    if option2_2_2 == "entrar" :
                        print("Entras al hangar junto al guia, pero al entrar puedes ver a otros aliens intentando abordar las naves, los guardias te atrapan y terminan contigo.")
                        win = False
                    elif option2_2_2 == "buscar" :
                        print("Decides buscar otra salida, dejando al guia atras. Encuentras una salida de emergencia y logras escapar de la nave, cayendo en un bosque lejano a tu casa.")
                        win = True
                    else :
                        print("tardas en tomar una decision y los guardias te atrapan")
                        win = False

                else : 
                    print("tardas en tomar una decision y los guardias te atrapan")

            elif option2 == "buscar" : 
                print("Decides buscar algo que te ayude a escapar. Mientras exploras la habitación, encuentras un objeto brillante en el suelo. Al acercarte, te das cuenta de que es un dispositivo de comunicación alienígena.")
                option2_2 = input("¿Qué harás? USAR o IGNORAR: ")

                if option2_2 == "usar" :
                    print("Usas el dispositivo de comunicación para enviar una señal de socorro, los otros humanos siguen pidiendo tu ayuda.")
                    option2_2_2 = input("¿Qué harás? ESPERAR o AYUDAR: ")

                    if option2_2_2 == "esperar" :
                        print("Decides esperar a que lleguen refuerzos, ignorando a los humanos atrapados. Despues de un tiempo puedes escuchar pasos en el pasillo, parece que la señal de alerta fue detectada por los guardias de la nave.")
                        win = False
                    elif option2_2_2 == "ayudar" :
                        print("Decides liberar a los humanos atrapados, los cuales no estan felices ante tu falta de compasion momentos antes. Eres retenido por los humanos y dejado en una camilla.")
                        win = False
                    else:
                        print("\n\nNo tomas ninguna acción válida y los guardias te encuentran y terminan contigo.")
                        win = False

                elif option2_2 == "ignorar" :
                    print("Decides ignorar el dispositivo y seguir buscando. Una pequeña esfera metálica llama tu atención.")
                    option2_2_2 = input("¿Qué harás? TOMAR o DEJAR: ")

                    if option2_2_2 == "tomar" :
                        print("Tomas la esfera y una luz brillante emana de ella, al recuperar tu vista, te encuentras en un lugar conocido, la esfera te ha teletransportado a la tierra.")
                        win = True
                    elif option2_2_2 == "dejar" :
                        print("Decides dejar la esfera y seguir buscando, pero no encuentras nada más de utilidad. Los guardias entran a la sala y te encuentran.")
                        win = False
                    else :
                        print("\n\nNo tomas ninguna acción válida y los guardias te encuentran y terminan contigo.")
                        win = False
                
                else:
                    print("Decides seguir buscando, pero no encuentra nada más de utilidad. Los guardias entran a la sala y te encuentran.")
                    win = False

            else:
                print("\n\n No tomas ninguna acción válida y los guardias te encuentran y terminan contigo.")
                win = False

        else:
            print("\n\nNo eliges ninguna acción, y los guardias entran a la sala y terminan contigo.")
            win = False

    else:
       print("\n\nNo eliges ningun pasillo, y los guardias te encuentran y terminan contigo. ")
       win = False  

# Mi parte :v (Luis) ↓

elif option1 == "esperar" :
    print("\n\nDecides esperar. Los aliens regresan y comienzan a discutir sobre ti en su idioma extraño. Finalmente, parecen dudar sobre qué hacer contigo.")
    option1_2 = input("\n\tQue haras? COOPERAR o RESISTIR: ").lower()

    if option1_2 == "cooperar" :
        print("\n\nLos aliens notan tu calma y deciden conducirte por un pasillo con dos puertas iluminadas y marcadas por simbolos, uno parecido a una 'x', el otro parecido a una 'y'.")
        option1_2_1 = input("\n\tPor cual puerta entraras? 'X' o 'Y': ").lower()

        if option1_2_1 == "x" :
            print("\n\nTras la puerta 'X', entras en una sala con una pantalla gigante mostrando imagenes de la Tierra. Un boton en la tabla de comandos esta a tu alcance.")
            option1_2_1_1 = input("\n\tQue haras? OBSERVAR o TOCAR: ").lower()

            if option1_2_1_1 == "observar" :
                print("\n\nLa pantalla cambia, mostrando imagenes de calma, destruccion y neutralidad. Los aliens parecen interesados en tu reaccion.")
                option1_2_1_1_1 = input("\n\tCuales te interesan mas? CALMA, DESTRUCCION o NEUTRALIDAD: ").lower()

                if option1_2_1_1_1 == "calma" :
                    print("\n\nLa imagen de calma crea un pequeño portal frente a ti. Parece que los aliens terminaron su investigacion contigo, quien sabe que habra tras ese portal.")
                    option1_2_1_1_1_1 = input("\n\tQue haras? ENTRAR o RECHAZAR: ").lower()

                    if option1_2_1_1_1_1 == "entrar" :
                        print("\n\nCruzas el portal y apareces en tu habitacion. La nave se desvanece del cielo.")
                        win = True
                    elif option1_2_1_1_1_1 == "rechazar" :
                        print("\n\nEl portal se colapsa. Los aliens consideran que prefieres mantenerte siendo investigado y te retienen.")
                        win = False
                    else :
                        print("\n\nDudas demasiado, el portal se cierra y un campo de contencion te inmoviliza.")
                        win = False

                elif option1_2_1_1_1 == "destruccion" :
                    print("\n\nUn pulso mental recorre tu cabeza, sientes comandos e instrucciones entrando a tu mente.")
                    option1_2_1_1_1_2 = input("\n\tComo reaccionas? ACEPTAR o RESISTIR: ").lower()

                    if option1_2_1_1_1_2 == "aceptar" :
                        print("\n\nAceptas la conexion, los aliens te envian de vuelta a la tierra con un proposito desconocido.")
                        win = True
                    elif option1_2_1_1_1_2 == "resistir" :
                        print("\n\nResistes como puedes los comandos e instrucciones. Los aliens ven tu resistencia y deciden seguir investigando.")
                        win = False
                    else :
                        print("\n\nTu mente colapsa entre señales contradictorias.")
                        win = False
                
                elif option1_2_1_1_1 == "neutralidad" :
                    print("\n\nLa imagen de neutralidad muestra un paisaje vacio y desolado. Los aliens parecen interesados en tu reaccion.")
                    option1_2_1_1_1_3 = input("\n\tComo reaccionas? INTRIGADO o ABURRIDO: ").lower()

                    if option1_2_1_1_1_3 == "intrigado" :
                        print("\n\nTu intriga es suficiente para los aliens, los cuales estudiaban el cerebro humano, parecen satisfechos con sus investigaciones y te devuelven a la tierra luego de borrar tu memoria.")
                        win = True

                    elif option1_2_1_1_1_3 == "aburrido" :
                        print("\n\nLa imagen de neutralidad no despierta tu interes. Los aliens deciden seguir investigando contigo.")
                        win = False

                else :
                    print("\n\nTu reaccion es inentendible, los aliens te consideran fallido y apagan la sala contigo dentro.")
                    win = False

            elif option1_2_1_1 == "tocar" :
                print("\n\nAl tocar el boton, la pantalla se apaga, los aliens te observan.")
                option1_2_1_1_2 = input("\n\tComo reaccionas? CONFUNDIDO o DESAFIANTE: ").lower()

                if option1_2_1_1_2 == "confundido" :
                    print("\n\nLos aliens no parecen descubrir lo que hiciste.")
                    option1_2_1_1_2_1 = input("\n\tMientras los aliens discuten, que haras? ESPERAR o ESCAPAR: ").lower()

                    if option1_2_1_1_2_1 == "esperar" :
                        print("\n\nEsperas pacientemente y los aliens terminan el experimento y te llevan a una capsula criogenica.")
                        win = False
                    elif option1_2_1_1_2_1 == "escapar" :
                        print("\n\nTu intento de escape es fallido, no eres capaz de liberarte de tus ataduras antes de que te envien a una capsula criogenica")
                        win = False
                    else :
                        print("\n\nLos aliens terminan su discousion y deciden que eres un sujeto no cooperativo.")
                        win = False

                elif option1_2_1_1_2 == "desafiante" :
                    print("\n\nLos aliens no aprecian tu actitud y te llevan al pasillo.")
                    option1_2_1_1_2_2 = input("\n\tQue haras? RESIGNARTE o LUCHAR: ").lower()

                    if option1_2_1_1_2_2 == "resignarte" :
                        print("\n\nAceptas tu destino y te llevan a una sala de contencion.")
                        win = False
                    elif option1_2_1_1_2_2 == "luchar" :
                        print("\n\nLuchas con todas tus fuerzas, pero los aliens son demasiado fuertes.")
                        win = False
                    else :
                        print("\n\nEres lanzado a una zona de desechos.")
                        win = False

                else :
                    print("\n\nLos aliens vieron tu mano en el boton y no aprecian tu accion. Eres confinado para observacion.")
                    win = False

            else :
                print("\n\nApartas la vista de la pantalla, tu falta de cooperacion te muestra como un especimen inutil y eres llevado a la zona de desechos.")
                win = False

        elif option1_2_1 == "y" :
            print("\n\nTras la puerta 'Y' hay jaulas con criaturas extraterrestres, los aliens te dejan frente a dos de ellas, una parecida a un insecto, otra parecida a un anfibio y la ultima no tiene una forma definida.")
            option1_2_1_2 = input("\n\tCual elegiras? INSECTO, ANFIBIO o SIN FORMA: ").lower()

            if option1_2_1_2 == "insecto" :
                print("\n\nEstiras la mano hacia la jaula del insecto, el cual acerca su cabeza a tu mano.")
                option1_2_1_2_1 = input("\n\tQue haras con tu mano? ACERCARLA o RETIRARLA: ").lower()

                if option1_2_1_2_1 == "acercarla" :
                    print("\n\nEl insecto acerca su cabeza a tu mano, mordiendote, puedes sentir un liquido correr por tus venas, no sabes si sera beneficioso o toxico.")
                    option1_2_1_2_1_1 = input("\n\tQue haras con tu mano? MANTENERLA o QUITARLA:  ").lower()

                    if option1_2_1_2_1_1 == "mantenerla" :
                        print("\n\nEl liquido comienza a hacer efecto, derritiendote desde adentro.")
                        win = False
                    elif option1_2_1_2_1_1 == "quitarla" :
                        print("\n\nRetiras tu mano, pero el liquido ya ha entrado a tu cuerpo, derrtiendo tu mano.")
                        win = False
                    else :
                        print("\n\nLos aliens cortan tu mano para evitar que el liquido se propague, dejandote incapacitado para mas experimentos.")
                        win = False

                elif option1_2_1_2_1 == "retirarla" :
                    print("\n\nRetiras tu mano a tiempo, el insecto choca con la jaula al intentar morderte. Los aliens revelan un boton para matar el insecto.")
                    option1_2_1_2_1_2 = input("\n\tQue haras? PRESIONARLO o IGNORARLO: ").lower()

                    if option1_2_1_2_1_2 == "presionarlo" :
                        print("\n\nPresionas el boton, el insecto muere, los aliens entienden tu reaccion y determinan que el experimento a concluido, liberandote.")
                        win = True
                    elif option1_2_1_2_1_2 == "ignorarlo" :
                        print("\n\nIgnoras el boton, el insecto sigue intentando morderte, los aliens deciden que eres un sujeto no cooperativo.")
                        win = False
                    else :
                        print("\n\nNo haces nada, el insecto consigue morderte y mueres por el veneno.")
                        win = False
                else :
                    print("\n\nNo haces nada, el insecto consigue morderte y mueres por el veneno.")
                    win = False

            elif option1_2_1_2 == "anfibio" :
                print("\n\nTe acercas a la jaula del anfibio, el cual te observa con curiosidad, te sientes atraido a acercar tu mano.")
                option1_2_1_2_2 = input("\n\tQue haras? ACERCAR o IGNORAR: ").lower()

                if option1_2_1_2_2 == "acercar" :
                    print("\n\nEl anfibio se acerca a tu mano, su piel es suave y gelatinosa, sientes una conexión telepática.")
                    option1_2_1_2_2_1 = input("\n\tQue haras? ALEJARTE o ESCUCHAR: ").lower()

                    if option1_2_1_2_2_1 == "alejarte" :
                        print("\n\nTe alejas lentamente, el anfibio te observa con tristeza. Los aliens parecen apreciar tu respuesta. Te liberan poco despues.")
                        win = True
                    elif option1_2_1_2_2_1 == "escuchar" :
                        print("\n\nTe concentras en la conexión telepática y comienzas a escuchar los pensamientos del anfibio, perdiendote en su mente.")
                        win = False
                    else :
                        print("\n\nNo reaccionas ante el anfibio, los aliens deciden que eres un sujeto no cooperativo.")
                        win = False

                elif option1_2_1_2_2 == "ignorar" :
                    print("\n\nIgnoras al anfibio. Al intentar mirar a otro lado, sientes una fuerza extraña en tu mente.")
                    option1_2_1_2_2_2 = input("\n\tQue haras? MIRARLO o IGNORARLO: ").lower()

                    if option1_2_1_2_2_2 == "mirarlo" :
                        print("\n\nMiras al anfibio a los ojos, no parece apreciar haber sido ignorado. Utiliza tu poder mental para destruir tu mente.")
                        win = False
                    elif option1_2_1_2_2_2 == "ignorarlo" :
                        print("\n\nIntentas ignorar al anfibio. Los aliens aprecian tu decision, cerrando la jaula del anfibio y liberandote.")
                        win = True
                    else :
                        print("\n\nNo tomas ninguna accion, los aliens deciden que eres un sujeto no cooperativo.")
                        win = False

                else :
                    print("\n\nNo haces nada, los aliens deciden que eres un sujeto no cooperativo.")
                    win = False

            elif option1_2_1_2 == "sin forma" :
                print("\n\nTe acercas a la jaula de la criatura sin forma, la cual se mueve y cambia su estructura constantemente.")
                option1_2_1_2_3 = input("\n\tQue haras? TOCAR o OBSERVAR: ").lower()

                if option1_2_1_2_3 == "tocar" :
                    print("\n\nAl tocar la criatura esta se afferra a ti, su masa gelatinosa comienza a cubrir tu mano.")
                    option1_2_1_2_3_1 = input("\n\tQue haras? QUITARLA o DEJARLA: ").lower()

                    if option1_2_1_2_3_1 == "quitarla" :
                        print("\n\nIntentas quitar la criatura de tu mano, su forma amorfa le permite salir de la jaula y esta sale volando hacia los aliens, los cuales son absorbidos por ella, en la conmocion, logras escapar de la nave y regresar a la tierra.")
                        win = True

                    elif option1_2_1_2_3_1 == "dejarla" :
                        print("\n\nDecides dejar a la criatura en paz, ella se acomoda en tu mano y parece estar tranquila. Eres consumido lentamente.")
                        win = False
                    else :
                        print("\n\nNo tomas ninguna accion, la criatura te consume lentamente.")
                        win = False

                elif option1_2_1_2_3 == "observar" :
                    print("\n\nObservas a la criatura, la cual cambia su forma constantemente, puedes ver como una parte de ella intenta escapar de la jaula, los aliens no parecen darse cuenta, quizas puedas alertarlos o dejar ir a la criatura.")
                    option1_2_1_2_3_2 = input("\n\tQue haras? ALERTAR o DEJARLA: ").lower()

                    if option1_2_1_2_3_2 == "alertar" :
                        print("\n\nAlertas a los aliens del escape de la criatura, la cual es neutralizada poco despues. Los experimentos continuan pero tu cooperacion los lleva por un buen camino, tu memoria es borrada y vuelves a la tierra.")
                        win = True
                    elif option1_2_1_2_3_2 == "dejarla" :
                        print("\n\nDecides no intervenir, distrayendo a los aliens momentaneamente, la criatura, sin embargo, no es capaz de entender tus acciones y te toma como su primera presa, los aliens consiguen terminarla con exito pero es muy tarde para ti.")
                        win = False
                    else :
                        print("\n\nNo tomas ninguna accion, los aliens deciden que eres un sujeto no cooperativo.")
                        win = False

                else :
                    print("\n\nNo haces nada, los aliens deciden que eres un sujeto no cooperativo.")
                    win = False

            else :
                print("\n\nNo haces nada, los aliens deciden que eres un sujeto no cooperativo.")
                win = False

        else :
            print("\n\nNo eliges ninguna puerta, te vuelven a sujetar a la camilla y te confinan para observacion.")
            win = False

    elif option1_2 == "resistir" :
        print("\n\nTe resistes con fuerza, sorprendiendo a los aliens. Uno abre dos compartimentos en la pared.")
        option1_2_2 = input("\n\tPor cual compartimento entraras? IZQUIERDO o DERECHO: ").lower()

        if option1_2_2 == "izquierdo" :
            print("\n\nEl compartimento izquierdo es una camara de simulacion.")
            option1_2_2_1 = input("\n\tQue haras? EXPLORAR o SALIR: ").lower()

            if option1_2_2_1 == "explorar" :
                print("\n\nLa simulacion muestra una ciudad futurista que responde a tu voluntad. Puedes intentar vivir en ella o buscar una forma de destruir la simulacion.")
                option1_2_2_1_1 = input("\n\tQue haras? VIVIR o DESTRUIR: ").lower()

                if option1_2_2_1_1 == "vivir" :
                    print("\n\nLa ciudad te ofrece un hogar perfecto. Realmente parece una ilusion placentera.")
                    option1_2_2_1_1_1 = input("\n\tAceptas? ACEPTAR o DESPERTAR: ").lower()

                    if option1_2_2_1_1_1 == "aceptar" :
                        print("\n\nAceptas la ilusion y vives una vida plena en la simulacion.")
                        win = True
                    elif option1_2_2_1_1_1 == "despertar" :
                        print("\n\nRechazas la ilusion, forzando un reinicio, los aliens te reciben molestos.")
                        win = False
                    else :
                        print("\n\nLa simulacion se corrompe y quedas atrapado.")
                        win = False

                elif option1_2_2_1_1 == "destruir" :
                    print("\n\nEncuentras vulnerabilidades en el entorno virtual. Puedes intentar escapar la simulacion o tomar tu tiempo para destruirla.")
                    option1_2_2_1_1_2 = input("\n\tAccion? HUIR o DESTRUIR: ").lower()

                    if option1_2_2_1_1_2 == "huir" :
                        print("\n\nAbres una brecha en el codigo y tu conciencia es transportada a la realidad. Los aliens parecen molestos ante tus acciones, confinandote nuevamente.")
                        win = False
                    elif option1_2_2_1_1_2 == "destruir" :
                        print("\n\nUtilizas tu poder sobre la simulacion para destruirla. Tus esfuerzos, sin embargo, son en vano, los aliens detienen la simulacion y te llevan a una capsula criogenica.")
                        win = False
                    else :
                        print("\n\nLa simulacion se corrompe y quedas atrapado.")
                        win = False

                else :
                    print("\n\nLa simulacion se corrompe y quedas atrapado.")
                    win = False

            elif option1_2_2_1 == "salir" :
                print("\n\nConsigues escapar la simulacion, tu cuerpo transportado a una camara de mantenimiento.")
                option1_2_2_1_2 = input("\n\tQue haras? CORRER o ESPERAR: ").lower()

                if option1_2_2_1_2 == "correr" :
                    print("\n\nEl corredor conectado a la camara lleva a una esclusa con sirenas activas.")
                    option1_2_2_1_2_1 = input("\n\tUltimo paso? CORRER o OCULTARTE: ").lower()

                    if option1_2_2_1_2_1 == "correr" :
                        print("\n\nCorres hasta un modulo de escape y despegas hacia la Tierra.")
                        win = True
                    elif option1_2_2_1_2_1 == "ocultarte" :
                        print("\n\nTe ocultas hasta que la seguridad de la nave te encuentra.")
                        win = False
                    else :
                        print("\n\nTe quedas inmovil y la seguridad de la nave te atrapa.")
                        win = False

                elif option1_2_2_1_2 == "esperar" :
                    print("\n\nTe quedas inmovil, escuchando pasos acercarse.")
                    option1_2_2_1_2_2 = input("\n\tPlan? PEDIR AYUDA o RENDIRTE: ").lower()

                    if option1_2_2_1_2_2 == "pedir ayuda" :
                        print("\n\nUn tecnico alien te escucha, alertando la seguridad de la nave de tu presencia.")
                        win = False
                    elif option1_2_2_1_2_2 == "rendirte" :
                        print("\n\nLevantas las manos, te recluyen permanentemente.")
                        win = False
                    else :
                        print("\n\nLa seguridad de la nave te encuentra y te atrapa.")
                        win = False

                else :
                    print("\n\nLa salida se sella y quedas atrapado.")
                    win = False

            else :
                print("\n\nTe quedas atrapado en la simulacion.")
                win = False

        elif option1_2_2 == "derecho" :
            print("\n\nEl compartimento derecho conduce a un hangar con dos naves pequenas. Los aliens parecen interesados en tu preferencia, la NAVE 1 es circular y la NAVE 2 es rectangular.")
            option1_2_2_2 = input("\n\tCual eliges? NAVE 1 o NAVE 2: ").lower()

            if option1_2_2_2 == "nave 1" :
                print("\n\nLa NAVE 1 esta operativa, pero los controles son indescifrables. Los aliens esperan tu decision.")
                option1_2_2_2_1 = input("\n\tPilotearas la nave? PILOTEAR o NO PILOTEAR: ").lower()

                if option1_2_2_2_1 == "pilotear" :
                    print("\n\nEl sistema se activa y traza una ruta segura. Parece pedir una altura de vuelo.")
                    option1_2_2_2_1_1 = input("\n\tAltura? ALTA ORBITA o BAJA ORBITA: ").lower()

                    if option1_2_2_2_1_1 == "alta orbita" :
                        print("\n\nTu decision de alta orbita es arriesgada, los aliens no parecen convencidos de tu inteligencia al tomar decisiones y detienen el experimento.")
                        win = False
                    elif option1_2_2_2_1_1 == "baja orbita" :
                        print("\n\nLos aliens parecen felices a tu decision, viendote como un experimento exitoso y dejandote ir.")
                        win = True
                    else :
                        print("\n\nElijes una altura de vuelo no válida, terminando el experimento.")
                        win = False

                elif option1_2_2_2_1 == "no pilotear" :
                    print("\n\nDecides no pilotear la nave, los aliens parecen decepcionados pero te permiten elegir otra opcion. Buscaras otra nave o te resignaras a tu destino.")
                    option1_2_2_2_1_2 = input("\n\tQue haras? BUSCAR OTRA NAVE o RESIGNARSE: ").lower()

                    if option1_2_2_2_1_2 == "buscar otra nave" :
                        print("\n\nNo encuentras otra nave, los aliens deciden que eres un experimento fallido.")
                        win = False
                    elif option1_2_2_2_1_2 == "resignarse" :
                        print("\n\nTe resignas a tu destino y esperas lo peor.")
                        win = False
                    else :
                        print("\n\nTu indecision molesta a los aliens.")
                        win = False

                else :
                    print("\n\nLa consola no reconoce tu orden y bloquea el despegue.")
                    win = False

            elif option1_2_2_2 == "nave 2" :
                print("\n\nLa NAVE 2 parpadea con alertas de averia. Ves algunos mecanismos expuestos, puedes intentar repararlos o pilotar la nave.")
                option1_2_2_2_2 = input("\n\tQue haras? REPARAR o ARRIESGAR: ").lower()

                if option1_2_2_2_2 == "reparar" :
                    print("\n\nConsigues estabilizar el reactor temporalmente.")
                    option1_2_2_2_2_1 = input("\n\tDespegar ahora? DESPEGAR o ABORTAR: ").lower()

                    if option1_2_2_2_2_1 == "despegar" :
                        print("\n\nLos aliens parecen satisfechos con tus desiciones, enviandote a la tierra.")
                        win = True
                    elif option1_2_2_2_2_1 == "abortar" :
                        print("\n\nAbortas el despegue y los aliens deciden que eres un experimento fallido.")
                        win = False
                    else :
                        print("\n\nLa reparacion falla y la nave colapsa.")
                        win = False

                elif option1_2_2_2_2 == "arriesgar" :
                    print("\n\nIntentas despegar tal cual, ignorando las alertas. Los aliens permiten que la nave despegue, pero las puertas no se han abierto.")
                    option1_2_2_2_2_2 = input("\n\t Que haras? EJECTAR o ACELERAR: ").lower()

                    if option1_2_2_2_2_2 == "ejectar" :
                        print("\n\nTe eyectas en el ultimo segundo y caes con un paracaidas de energia de vuelta en el hangar.")
                        win = False
                    elif option1_2_2_2_2_2 == "acelerar" :
                        print("\n\nEl motor explota, destruyendo la nave contigo adentro.")
                        win = False
                    else :
                        print("\n\nNo decides y el sistema te apaga por seguridad.")
                        win = False

                else :
                    print("\n\nLa nave no responde a los controles.")
                    win = False

            else :
                print("\n\nNo eres capaz de elegir una nave, los aliens se cansan de esperar.")
                win = False

        else :
            print("\n\nNo eliges un compartimento, los aliens te confinan para observacion.")
            win = False

    else :
        print("\n\nLos aliens no entienden tu respuesta, te confinan para observacion.")
        win = False

else :
    print("\n\nNo eliges una accion, los aliens te mantienen en animacion suspendida.")
    win = False

if win == True :
    print("\n\n\t\tHAS SOBREVIVIDO.")
elif win == False :
    print("\n\n\t\tHAS PERDIDO.")