import numpy as np
import pandas as pd
class tablero_defensa_jugador():
    '''
    Genera un tablero vacio de 10x10 casillas a través de numpy. Inicialmente todas las posiciones se corresponden con agua. \n
    El objeto tablero_defensa presenta 3 atributos: coordenadas longitudinales (horizontal, letras A hasta J), coordenadas latitudinales (verticales, de 0 a 9), la matriz que actua como cuadrícula y las vidas que tiene cada flota antes de ser aniquilada.
    Los métodos incluidos en este objeto sirven para colocar los diferentes barcos, que incluyen:\n
    > 4 fragatas de 1 casilla cada una.\n> 3 destructores de 2 posiciones.\n> 2 acorazados de 3 posiciones en el mapa. \n> 1 portaaviones de 4 casillas.\n
    '''
    coord_long = ['A','B','C','D','E','F','G','H','I','J']
    coord_lat = [0 ,1 ,2, 3, 4, 5, 6, 7 , 8 , 9]
    mapa = pd.DataFrame(np.array(100*['.']).reshape(10 , 10) , index=coord_lat , columns=coord_long)
    vidas = 20
    def posiciones_fragatas(self):
        '''
        Método que contiene dos bucles tipo 'while True' para introducir la posición de 4 fragatas de 1 posicion cada una a través de un input específico de cada una. \n
        Cada bucle se rompe cuando las posiciones han sido introducidas correctamente (dentro del plano y en orden apropiado (A-J,0-9) y sin superponer los barcos con otros ya establecidos en el mapa; además de que solo se aceptan distribuciones contiguas verticales y horizontales.)
        '''
        #Bucle para posiciones de las fragatas:
        for i in range(1,5):
            while True:
                fragata_i = (input("Fragata " + str(i) +" de 4 (A-J,0-9): ").upper())
                fragata_i = fragata_i.split(",")

                #Comprobacion de longitud correcta de las coordenadas.
                if len(fragata_i)==2:
                    
                    #Comprobación de que cada elemento se ha introducido en el orden correcto y está dentro de los rangos establecidos.
                    #Incluye un 'try' para evitar que el codigo se rompa si se intenta generar un integer de una letra.
                    try:
                        if (fragata_i[0] in self.coord_long and int(fragata_i[1]) in self.coord_lat):

                            #Comprobacion de que las coordenadas elegidas están disponibles para colocar un barco.
                            if (self.mapa.loc[int(fragata_i[1]),fragata_i[0]]) == ".":

                                #Colocación del barco
                                self.mapa.loc[int(fragata_i[1]),fragata_i[0]]='F'
                                break
                            else:
                                print('Ya hay un barco en la posición asignada')
                        else:
                            print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
                    except:
                        print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
                else:
                    print("Introducir solo una coordenada del plano.")
            print(self.mapa)

    def posiciones_destructores(self):
        '''
        Método que contiene dos bucles tipo 'while True' para introducir la posición de 3 destructores de 2 posiciones cada uno a través de un input específico de cada uno. \n
        Cada bucle se rompe cuando las posiciones han sido introducidas correctamente (dentro del plano y en orden apropiado (A-J,0-9,A-J,0-9) y sin superponer los barcos con otros ya establecidos en el mapa; además de que solo se aceptan distribuciones contiguas verticales y horizontales.)
        '''

        #Bucle para posicion de los destructores:
        for i in range(1,4):
            while True:
                destructor_i = (input("Destructor "+ str(i) + " de 3 (A-J,0-9,A-J,0-9): ").upper())
                destructor_i = destructor_i.split(",")
                #Comprobacion de longitud correcta de las coordenadas.
                if len(destructor_i)==4:
                    
                    #Comprobación de que cada elemento se ha introducido en el orden correcto y está dentro de los rangos establecidos.
                    #Incluye un 'try' para evitar que el codigo se rompa si se intenta generar un integer de una letra.
                    try:
                        if (destructor_i[0] in self.coord_long and int(destructor_i[1]) in self.coord_lat) and (destructor_i[2] in self.coord_long and int(destructor_i[3]) in self.coord_lat):
                            
                            #Comprobacion de que las coordenadas elegidas están disponibles para colocar un barco.
                            if (self.mapa.loc[int(destructor_i[1]),destructor_i[0]] == '.') and (self.mapa.loc[int(destructor_i[3]),destructor_i[2]] == '.'):
                                
                                #Comprobación de que las posiciones escogidas son contiguas en la vertical o en la horizontal.
                                letra_contigua = (self.coord_long.index(destructor_i[0]) == self.coord_long.index(destructor_i[2])+1) or (self.coord_long.index(destructor_i[0]) == self.coord_long.index(destructor_i[2])-1)
                                numero_contiguo = ((self.coord_lat.index(int(destructor_i[1])) == self.coord_lat.index(int(destructor_i[3]))+1) or (self.coord_lat.index(int(destructor_i[1])) == self.coord_lat.index(int(destructor_i[3]))-1))
                                
                                #Las siguientes comprobaciones incluyen que no se permitan posiciones en diagonal.
                                if (letra_contigua or numero_contiguo) and not(letra_contigua and numero_contiguo):
                                    self.mapa.loc[int(destructor_i[1]),destructor_i[0]] = 'D'
                                    self.mapa.loc[int(destructor_i[3]),destructor_i[2]] = 'D'
                                    break
                                else:
                                    print('Las posiciones deben ser contiguas en la horizontal o vertical.')
                            else:
                                print('Ya hay un barco en la posición asignada')
                        else:
                            print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
                    except:
                        print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
                else:
                    print("Se deben introducir dos posiciones en el plano.")
            print(self.mapa)

    def posiciones_acorazados(self):
        '''
        Método que contiene dos bucles tipo 'while True' para introducir la posición de 2 acorazados de 3 posiciones cada uno a través de un input específico de cada uno. \n
        Cada bucle se rompe cuando las posiciones han sido introducidas correctamente (dentro del plano y en orden apropiado (A-J,0-9,A-J,0-9,A-J,0-9) y sin superponer los barcos con otros ya establecidos en el mapa; además de que solo se aceptan distribuciones contiguas verticales y horizontales.)
        '''
        #Bucle para posicione de los acorazados:
        for i in range(1,3):
            while True:
                acorazado_i = (input("Acorazado " + str(i) + " de 2 (A-J,0-9,A-J,0-9,A-J,0-9): ").upper())
                acorazado_i = acorazado_i.split(",")
                #Comprobacion de longitud correcta de las coordenadas.
                if len(acorazado_i)==6:
                    
                    #Comprobación de que cada elemento se ha introducido en el orden correcto y está dentro de los rangos establecidos.
                    #Incluye un 'try' para evitar que el codigo se rompa si se intenta generar un integer de una letra.
                    try:
                        if (acorazado_i[0] in self.coord_long and int(acorazado_i[1]) in self.coord_lat) and (acorazado_i[2] in self.coord_long and int(acorazado_i[3]) in self.coord_lat) and (acorazado_i[4] in self.coord_long and int(acorazado_i[5]) in self.coord_lat):
                            
                            #Comprobacion de que las coordenadas elegidas están disponibles para colocar un barco.
                            if (self.mapa.loc[int(acorazado_i[1]),acorazado_i[0]] == '.') and (self.mapa.loc[int(acorazado_i[3]),acorazado_i[2]] == '.') and (self.mapa.loc[int(acorazado_i[5]),acorazado_i[4]] == '.'):
                                
                                #Comprobación de que las posiciones escogidas son contiguas en la vertical o en la horizontal.
                                letra12_contiguas = ((self.coord_long.index(acorazado_i[0]) == self.coord_long.index(acorazado_i[2])+1) or (self.coord_long.index(acorazado_i[0]) == self.coord_long.index(acorazado_i[2])-1)) 
                                letra23_contiguas = ((self.coord_long.index(acorazado_i[2]) == self.coord_long.index(acorazado_i[4])+1) or (self.coord_long.index(acorazado_i[2]) == self.coord_long.index(acorazado_i[4])-1))
                                numeros12_contiguos = ((self.coord_lat.index(int(acorazado_i[1])) == self.coord_lat.index(int(acorazado_i[3]))+1) or (self.coord_lat.index(int(acorazado_i[1])) == self.coord_lat.index(int(acorazado_i[3]))-1)) 
                                numeros23_contiguos = ((self.coord_lat.index(int(acorazado_i[3])) == self.coord_lat.index(int(acorazado_i[5]))+1) or (self.coord_lat.index(int(acorazado_i[3])) == self.coord_lat.index(int(acorazado_i[5]))-1))
                                
                                letras_contiguas = letra12_contiguas and letra23_contiguas
                                numeros_contiguos = numeros12_contiguos and numeros23_contiguos
                                
                                #Las siguientes comprobaciones incluyen que no se permitan posiciones en diagonal.
                                if letras_contiguas and (acorazado_i[1] == acorazado_i[3] == acorazado_i[5]):
                                    #Colocación del barco en horizontal
                                    self.mapa.loc[int(acorazado_i[1]),acorazado_i[0]] = 'A'
                                    self.mapa.loc[int(acorazado_i[3]),acorazado_i[2]] = 'A'
                                    self.mapa.loc[int(acorazado_i[5]),acorazado_i[4]] = 'A'
                                    break
                                elif numeros_contiguos and (acorazado_i[0] == acorazado_i[2] == acorazado_i[4]):
                                    #Colocación del barco en vertical
                                    self.mapa.loc[int(acorazado_i[1]),acorazado_i[0]] = 'A'
                                    self.mapa.loc[int(acorazado_i[3]),acorazado_i[2]] = 'A'
                                    self.mapa.loc[int(acorazado_i[5]),acorazado_i[4]] = 'A'
                                    break
                                else:
                                    print('Las posiciones deben ser contiguas en la horizontal o vertical.')
                            else:
                                print('Ya hay un barco en la posición asignada')
                        else:
                            print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
                    except:
                        print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
                else:
                    print("Se deben introducir tres posiciones en el plano.")
            print(self.mapa)

    def posicion_portaviones(self):
        #Bucle para posicion del portaviones:
        while True:
            portaviones = (input("Portaviones (A-J,0-9,A-J,0-9,A-J,0-9,A-J,0-9): ").upper())
            portaviones = portaviones.split(",")
            #Comprobacion de longitud correcta de las coordenadas.
            if len(portaviones)==8:
                
                #Comprobación de que cada elemento se ha introducido en el orden correcto y está dentro de los rangos establecidos.
                #Incluye un 'try' para evitar que el codigo se rompa si se intenta generar un integer de una letra.
                try:
                    if (portaviones[0] in self.coord_long and int(portaviones[1]) in self.coord_lat) and (portaviones[2] in self.coord_long and int(portaviones[3]) in self.coord_lat) and (portaviones[4] in self.coord_long and int(portaviones[5]) in self.coord_lat) and (portaviones[6] in self.coord_long and int(portaviones[7]) in self.coord_lat):
                        
                        #Comprobacion de que las coordenadas elegidas están disponibles para colocar un barco.
                        if (self.mapa.loc[int(portaviones[1]),portaviones[0]] == '.') and (self.mapa.loc[int(portaviones[3]),portaviones[2]] == '.') and (self.mapa.loc[int(portaviones[5]),portaviones[4]] == '.'):
                            
                            #Comprobación de que las posiciones escogidas son contiguas en la vertical o en la horizontal.
                            letra12_contiguas = ((self.coord_long.index(portaviones[0]) == self.coord_long.index(portaviones[2])+1) or (self.coord_long.index(portaviones[0]) == self.coord_long.index(portaviones[2])-1)) 
                            letra23_contiguas = ((self.coord_long.index(portaviones[2]) == self.coord_long.index(portaviones[4])+1) or (self.coord_long.index(portaviones[2]) == self.coord_long.index(portaviones[4])-1))
                            letra34_contiguas = ((self.coord_long.index(portaviones[4]) == self.coord_long.index(portaviones[6])+1) or (self.coord_long.index(portaviones[4]) == self.coord_long.index(portaviones[6])-1))
                            
                            numeros12_contiguos = ((self.coord_lat.index(int(portaviones[1])) == self.coord_lat.index(int(portaviones[3]))+1) or (self.coord_lat.index(int(portaviones[1])) == self.coord_lat.index(int(portaviones[3]))-1)) 
                            numeros23_contiguos = ((self.coord_lat.index(int(portaviones[3])) == self.coord_lat.index(int(portaviones[5]))+1) or (self.coord_lat.index(int(portaviones[3])) == self.coord_lat.index(int(portaviones[5]))-1))
                            numeros34_contiguos = ((self.coord_lat.index(int(portaviones[5])) == self.coord_lat.index(int(portaviones[7]))+1) or (self.coord_lat.index(int(portaviones[5])) == self.coord_lat.index(int(portaviones[7]))-1))
                            
                            letras_contiguas = letra12_contiguas and letra23_contiguas and letra34_contiguas
                            numeros_contiguos = numeros12_contiguos and numeros23_contiguos and numeros34_contiguos
                            
                            #Las siguientes comprobaciones incluyen que no se permitan posiciones en diagonal.
                            if letras_contiguas and (portaviones[1] == portaviones[3] == portaviones[5] == portaviones[7]):
                                #Colocar varco en la horizontal
                                self.mapa.loc[int(portaviones[1]),portaviones[0]] = 'P'
                                self.mapa.loc[int(portaviones[3]),portaviones[2]] = 'P'
                                self.mapa.loc[int(portaviones[5]),portaviones[4]] = 'P'
                                self.mapa.loc[int(portaviones[7]),portaviones[6]] = 'P'
                                break
                            elif numeros_contiguos and (portaviones[0] == portaviones[2] == portaviones[4] == portaviones[6]):
                                #Colocar barco en la vertical
                                self.mapa.loc[int(portaviones[1]),portaviones[0]] = 'P'
                                self.mapa.loc[int(portaviones[3]),portaviones[2]] = 'P'
                                self.mapa.loc[int(portaviones[5]),portaviones[4]] = 'P'
                                self.mapa.loc[int(portaviones[7]),portaviones[6]] = 'P'
                                break
                            else:
                                print('Las posiciones deben ser contiguas en la horizontal o vertical.')
                        else:
                            print('Ya hay un barco en la posición asignada')
                    else:
                        print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
                except:
                    print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
            else:
                print("Se deben introducir cuatro posiciones en el plano.")
        print(self.mapa)







def colocar_barcos_jugador():
    '''
    Función que permite crear el mapa del jugador y que este coloque sus barcos. \n
    Utiliza la clase 'tablero_defensa_jugador' y sus métodos 'posicion_portaviones', 'posiciones_acorazados' , 'posiciones_destructores' y 'posiciones_fragatas'.
    '''
    jugador_t = tablero_defensa_jugador()
    print(jugador_t.mapa)
    print()

    jugador_t.posicion_portaviones()
    jugador_t.posiciones_acorazados()
    jugador_t.posiciones_destructores()
    jugador_t.posiciones_fragatas()

    print()
    print(jugador_t.mapa)


#Inicio de la partida
colocar_barcos_jugador()