import numpy as np
import pandas as pd
class tablero_defensa_jugador():
    '''
    Genera un tablero vacio de 10x10 casillas a través de numpy. Inicialmente todas las posiciones se corresponden con agua. \n
    El objeto tablero_defensa presenta 3 atributos: coordenadas longitudinales (horizontal, letras A hasta J), coordenadas latitudinales (verticales, de 0 a 9) y la matriz que actua como cuadrícula.
    Los métodos incluidos en este objeto sirven para colocar los diferentes barcos, que incluyen:\n
    4 fragatas de 1 casilla cada una.\n3 destructores de 2 posiciones.\n2 acorazados de 3 posiciones en el mapa. \n1 portaaviones de 4 casillas.\n
    '''
    coord_long = ['A','B','C','D','E','F','G','H','I','J']
    coord_lat = [0 ,1 ,2, 3, 4, 5, 6, 7 , 8 , 9]
    mapa = pd.DataFrame(np.array(100*['.']).reshape(10 , 10) , index=coord_lat , columns=coord_long)
    def posiciones_fragatas(self):
        '''
        Establece la posición de 4 fragatas (1 casilla cada una). Acepta 4 inputs basados en una estructura 'letra,número' dentro de los rangos establecidos.
        '''
        #Bucle para posición de la fragata_1:
        while True:
            fragata_1 = (input("Fragata 1 de 4 (A-J,0-9): ").upper())
            fragata_1 = fragata_1.split(",")
            print(fragata_1 , fragata_1[0], fragata_1[1])
            if (fragata_1[0] in self.coord_long and int(fragata_1[1]) in self.coord_lat):
                self.mapa[self.coord_long.index(fragata_1[0]) , self.coord_lat.index(int(fragata_1[1]))] = 'F'
                break
            else:
                print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
        #Bucle para posición de la fragata_2:
        while True:
            fragata_2 = (input("Fragata 2 de 4 (A-J,0-9): ").upper())
            fragata_2 = fragata_2.split(",")
            print(fragata_2 , fragata_2[0], fragata_2[1])
            if (fragata_2[0] in self.coord_long and int(fragata_2[1]) in self.coord_lat):
                if (self.mapa[self.coord_long.index(fragata_2[0]) , self.coord_lat.index(int(fragata_2[1]))]) == '.':
                    self.mapa[self.coord_long.index(fragata_2[0]) , self.coord_lat.index(int(fragata_2[1]))] = 'F'
                    break
                else:
                    print('Ya hay un barco en la posición asignada')
            else:
                print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
        #Bucle para posición de la fragata_3:
        while True:
            fragata_3 = (input("Fragata 3 de 4 (A-J,0-9): ").upper())
            fragata_3 = fragata_3.split(",")
            print(fragata_3 , fragata_3[0], fragata_3[1])
            if (fragata_3[0] in self.coord_long and int(fragata_3[1]) in self.coord_lat):
                if (self.mapa[self.coord_long.index(fragata_3[0]) , self.coord_lat.index(int(fragata_3[1]))]) == '.':
                    self.mapa[self.coord_long.index(fragata_3[0]) , self.coord_lat.index(int(fragata_3[1]))] = 'F'
                    break
                else:
                    print('Ya hay un barco en la posición asignada')
            else:
                print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
        #Bucle para posición de la fragata_4:
        while True:
            fragata_4 = (input("Fragata 4 de 4 (A-J,0-9): ").upper())
            fragata_4 = fragata_4.split(",")
            print(fragata_4 , fragata_4[0], fragata_4[1])
            if (fragata_4[0] in self.coord_long and int(fragata_4[1]) in self.coord_lat):
                if (self.mapa[self.coord_long.index(fragata_4[0]) , self.coord_lat.index(int(fragata_4[1]))]) == '.':
                    self.mapa[self.coord_long.index(fragata_4[0]) , self.coord_lat.index(int(fragata_4[1]))] = 'F'
                    break
                else:
                    print('Ya hay un barco en la posición asignada')
            else:
                print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
        print(self.mapa)
#    def posiciones_destructores():
        #Bucle para colocar el destructor_1:



jugador_t = tablero_defensa_jugador()
jugador_t.posiciones_fragatas()
