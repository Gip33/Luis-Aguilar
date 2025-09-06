import os
os.system("cls")
win = False

print("\n\nUna fuerte luz invade tu habitacion en la mitad de la noche, una fuerza mueve tu cuerpo a traves del edificio en el que vives, tu cuerpo se vuelve intangible y es transportado a traves de un rayo de luz a una gigantesca nave espacial. Al llegar al final del rayo de luz una luz blanca te ciega y te encuentras atrapado en una camilla de metal, un grupo de aliens estan hablando en un idioma que no entiendes y dejan la habitacion un tiempo luego.")
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

            elif option1_1_1_1 == "circulo" :
                print("\n\nTomaste el circulo, el mango evita que tu mano se derrita por el material viscoso. Puedes intentar derretir los motores o la pared de la nave.")
                option1_1_1_1_2 = input("\n\tQue derretiras? MOTORES o PARED: ").lower()

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
                print("\n\nLa pantalla cambia, mostrando imagenes de calma y destruccion. Los aliens parecen interesados en tu reaccion.")
                option1_2_1_1_1 = input("\n\tCuales te interesan mas? CALMA o DESTRUCCION: ").lower()

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
            print("\n\nTras la puerta 'Y' hay jaulas con criaturas extraterrestres, los aliens te dejan frente a dos de ellas, una parecida a un insecto, la otra parecida a un anfibio.")
            option1_2_1_2 = input("\n\tCual elegiras? INSECTO o ANFIBIO: ").lower()

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