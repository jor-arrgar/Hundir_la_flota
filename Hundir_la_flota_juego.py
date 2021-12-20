print("¡Bienvenido al juego 'Hundir la flota'! \n")
print("Este juego ha sido creado por Jorge Arranz , Jon Benito y David Guix. \nA continuación se explican las instrucciones para jugar a los clasicos barquitos :)")



print("El juego consta de tres niveles diferentes: \n")
print()
print("1ª GUERRA MUNDIAL \nEl juego de hundir la flota clásico. Coloca los barcos en sus posiciones y realiza ataques a coordenadas individuales. \n")
print("2ª GUERRA MUNDIAL \nLos tiempos avanzan, y con ellos la tecnología. Además del ataque a una única coordenada, dispones de la posibilidad de realizar hasta 2 ataques aéreos que barrerán una fila o una columna entera. La flota enemiga también dispone de ellos, así que cuidado con como colocas los barcos de tu flota. \n")
print("3ª GUERRA MUNDIAL \n¡El avanze de la tecnología es imparable! El desarrollo de los motores a reacción y de la electrónica han permitido colocar armas en satélites en órbita. Derrota a la flota enemiga antes de que sus equipos de guerra electrónica accedan a estas armas y las utilicen para barrer sectores enteros de tu tablero. Lamentablemente, tus equipos de guerra informática no son lo suficientemente avanzados para disponer de este tipo de ataques, pero si para evitar alguno de ellos en tu contra, ¡suerte! \n")
print()
print("A continuación se mostrará un menú de elección de modo de juego:")

import Hundir_la_flota_clases_y_funciones as cf

while True:
    cf.reset() #Reestablece los parámetro iniciales de la clase (limpia tableros y contadores)
    print("Elija el modo de juego a través de los siguientes comandos: \n\n1ª GUERRA MUNDIAL ==> 1 \n2ª GUERRA MUNDIAL ==> 2 \n3ª GUERRA MUNDIAL ==> 3 \nSalir del juego ==> 0") #Menú interactivo de eleccion de nivel y de cerrar el juego
    modo_de_juego = input("Modo de juego: ")
    cf.colocar_barcos() # Permite colocar los barcos tanto al jugador como a la máquina
    if modo_de_juego == '1': # 1ª Guerra Mundial

        while (cf.jugador.vida_jugador > 0) or (cf.maquina.vida_maquina > 0): #Bucle de juego
            continuar = input("Pulse cualquier tecla para continuar, pulse 0 para salir del modo de juego: ")
            if continuar != '0':
                cf.disparo_jugador()
                print("Vidas de la máquina: " , cf.maquina.vida_maquina)
                cf.disparo_maquina()
                print("vidas del jugador: " , cf.jugador.vida_jugador)
                while True:
                    mostrar_mapa = input("Pulsa 'D' para mostrar tu tablero de defensa, 'A' para mostrar el tablero con las posiciones que has atacado o '0' para continuar: ")
                    if mostrar_mapa == 'D' or mostrar_mapa == 'd':
                        print(cf.jugador.mapa_defensa_j)
                    elif mostrar_mapa == 'A' or mostrar_mapa == 'a':
                        print(cf.jugador.mapa_ataque_j)
                    elif mostrar_mapa == '0':
                        break
                    else:
                        print('Comando no válido.')
            else:
                break
        if cf.jugador.vida_jugador == 0:
            print('Tu flota ha sido destruida. Has perdido la partida.')
        elif cf.maquina.vida_maquina == 0:
            print('¡Enhorabuena! Has derrotado a la flota enemiga.')
    
    elif modo_de_juego == '2': # 2ª Guerra Mundial

        while (cf.jugador.vida_jugador > 0) or (cf.maquina.vida_maquina > 0):
            continuar = input("Pulse cualquier tecla para continuar, pulse 0 para salir del modo de juego: ")
            if continuar != '0':
                cf.ataque_aereo_jugador()
                cf.disparo_jugador()
                print("Vidas de la máquina: " , cf.maquina.vida_maquina)
                cf.ataque_aereo_maquina()
                cf.disparo_maquina()
                print("vidas del jugador: " , cf.jugador.vida_jugador)
                while True:
                    mostrar_mapa = input("Pulsa 'D' para mostrar tu tablero de defensa, 'A' para mostrar el tablero con las posiciones que has atacado o pulse la tecla 'ENTER' para continuar: ")
                    if mostrar_mapa == 'D' or mostrar_mapa == 'd':
                        print(cf.jugador.mapa_defensa_j)
                    elif mostrar_mapa == 'A' or mostrar_mapa == 'a':
                        print(cf.jugador.mapa_ataque_j)
                    elif mostrar_mapa == '':
                        break
                    else:
                        print('Comando no válido.')
            else:
                break
        if cf.jugador.vida_jugador == 0:
            print('Tu flota ha sido destruida. Has perdido la partida.')
        elif cf.maquina.vida_maquina == 0:
            print('¡Enhorabuena! Has derrotado a la flota enemiga.')

    elif modo_de_juego == '3': # 3ª Guerra Mundial

        cuenta_atras = 0
        while (cf.jugador.vida_jugador > 0) or (cf.maquina.vida_maquina > 0):
            continuar = input("Pulse cualquier tecla para continuar, pulse 0 para salir del modo de juego: ")
            if continuar != '0':
                if cuenta_atras < 8:
                    cf.ataque_aereo_jugador()
                    cf.disparo_jugador()
                    print("Vidas de la máquina: " , cf.maquina.vida_maquina)
                    cf.ataque_aereo_maquina()
                    cf.disparo_maquina()
                    print("vidas del jugador: " , cf.jugador.vida_jugador)
                    cuenta_atras += 1
                    print("Rondas: " , cuenta_atras)
                    while True:
                        mostrar_mapa = input("Pulsa 'D' para mostrar tu tablero de defensa, 'A' para mostrar el tablero con las posiciones que has atacado o pulse la tecla 'ENTER' para continuar: ")
                        if mostrar_mapa == 'D' or mostrar_mapa == 'd':
                            print(cf.jugador.mapa_defensa_j)
                        elif mostrar_mapa == 'A' or mostrar_mapa == 'a':
                            print(cf.jugador.mapa_ataque_j)
                        elif mostrar_mapa == '':
                            break
                        else:
                            print('Comando no válido.')
                elif cuenta_atras == 9 or cuenta_atras == 10:
                    print("¡Atención! ¡La flota enemiga está a punto de acceder a los sistemas de guerra espacial!")
                    cf.ataque_aereo_jugador()
                    cf.disparo_jugador()
                    print("Vidas de la máquina: " , cf.maquina.vida_maquina)
                    cf.ataque_aereo_maquina()
                    cf.disparo_maquina()
                    print("vidas del jugador: " , cf.jugador.vida_jugador)
                    cuenta_atras += 1
                    print("Rondas: " , cuenta_atras)
                    while True:
                        mostrar_mapa = input("Pulsa 'D' para mostrar tu tablero de defensa, 'A' para mostrar el tablero con las posiciones que has atacado o pulse la tecla 'ENTER' para continuar: ")
                        if mostrar_mapa == 'D' or mostrar_mapa == 'd':
                            print(cf.jugador.mapa_defensa_j)
                        elif mostrar_mapa == 'A' or mostrar_mapa == 'a':
                            print(cf.jugador.mapa_ataque_j)
                        elif mostrar_mapa == '':
                            break
                        else:
                            print('Comando no válido.')
                elif cuenta_atras == 11:
                    print("¡ATENCIÓN! ¡LA FLOTA ENEMIGA HA TOMADO EL CONTROL DE ARMAS ORBITALES! \n¡Date prisa en derrotarla o estarás acabado en un abrir y cerrar de ojos!")
                    cf.ataque_aereo_jugador()
                    cf.disparo_jugador()
                    print("Vidas de la máquina: " , cf.maquina.vida_maquina)
                    cf.ataque_orbital()
                    cf.ataque_aereo_maquina()
                    cf.disparo_maquina()
                    print("vidas del jugador: " , cf.jugador.vida_jugador)
                    cuenta_atras += 1
                    print("Rondas: " , cuenta_atras)
                    while True:
                        mostrar_mapa = input("Pulsa 'D' para mostrar tu tablero de defensa, 'A' para mostrar el tablero con las posiciones que has atacado o pulse la tecla 'ENTER' para continuar: ")
                        if mostrar_mapa == 'D' or mostrar_mapa == 'd':
                            print(cf.jugador.mapa_defensa_j)
                        elif mostrar_mapa == 'A' or mostrar_mapa == 'a':
                            print(cf.jugador.mapa_ataque_j)
                        elif mostrar_mapa == '':
                            break
                        else:
                            print('Comando no válido.')
                else:
                    print("¡LA FLOTA ENEMIGA TIENE EL CONTROL DE ARMAS ORBITALES!")
                    cf.ataque_aereo_jugador()
                    cf.disparo_jugador()
                    print("Vidas de la máquina: " , cf.maquina.vida_maquina)
                    cf.ataque_orbital()
                    cf.ataque_aereo_maquina()
                    cf.disparo_maquina()
                    print("vidas del jugador: " , cf.jugador.vida_jugador)
                    cuenta_atras += 1
                    print("Rondas: " , cuenta_atras)
                    while True:
                        mostrar_mapa = input("Pulsa 'D' para mostrar tu tablero de defensa, 'A' para mostrar el tablero con las posiciones que has atacado o pulse la tecla 'ENTER' para continuar: ")
                        if mostrar_mapa == 'D' or mostrar_mapa == 'd':
                            print(cf.jugador.mapa_defensa_j)
                        elif mostrar_mapa == 'A' or mostrar_mapa == 'a':
                            print(cf.jugador.mapa_ataque_j)
                        elif mostrar_mapa == '':
                            break
                        else:
                            print('Comando no válido.')
            else:
                break
        if cf.jugador.vida_jugador == 0:
            print('Tu flota ha sido destruida. Has perdido la partida.')
        elif cf.maquina.vida_maquina == 0:
            print('¡Enhorabuena! Has derrotado a la flota enemiga.')
    
    elif modo_de_juego == '0': # Cierra el juego y finaliza la lectura de código
        print('Hasta la próxima partida.')
        break