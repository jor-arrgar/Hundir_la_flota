import numpy as np
import pandas as pd
class tablero_defensa_jugador():
    '''
    Genera un tablero vacio de 10x10 casillas a través de numpy. Inicialmente todas las posiciones se corresponden con agua. \n
    El objeto tablero_defensa presenta 3 atributos: coordenadas longitudinales (horizontal, letras A hasta J), coordenadas latitudinales (verticales, de 0 a 9) y la matriz que actua como cuadrícula.
    Los métodos incluidos en este objeto sirven para colocar los diferentes barcos, que incluyen:\n
    > 4 fragatas de 1 casilla cada una.\n> 3 destructores de 2 posiciones.\n> 2 acorazados de 3 posiciones en el mapa. \n> 1 portaaviones de 4 casillas.\n
    '''
    coord_long = ['A','B','C','D','E','F','G','H','I','J']
    coord_lat = [0 ,1 ,2, 3, 4, 5, 6, 7 , 8 , 9]
    mapa = pd.DataFrame(np.array(100*['.']).reshape(10 , 10) , index=coord_lat , columns=coord_long)
    def posiciones_fragatas(self):
        '''
        Establece la posición de 4 fragatas (1 casilla cada una). Acepta 4 inputs basados en una estructura 'letra,número' dentro de los rangos establecidos siempre que la casilla elegida no presente otro barco.
        '''
        #Bucle para posición de la fragata_1:
        while True:
            fragata_1 = (input("Fragata 1 de 4 (A-J,0-9): ").upper())
            fragata_1 = fragata_1.split(",")
            if len(fragata_1)==2:
                print(fragata_1 , fragata_1[0], fragata_1[1])
            
                if (fragata_1[0] in self.coord_long and int(fragata_1[1]) in self.coord_lat):
                    if (self.mapa.loc[int(fragata_1[1]),fragata_1[0]]) == ".":
                        self.mapa.loc[int(fragata_1[1]),fragata_1[0]]='F'
                        break
                    else:
                        print('Ya hay un barco en la posición asignada')
                else:
                    print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
            else:
                print("Introducir solo una coordenada del plano.")
        print(self.mapa)

        #Bucle para posición de la fragata_2:
        while True:
            fragata_2 = (input("Fragata 2 de 4 (A-J,0-9): ").upper())
            fragata_2 = fragata_2.split(",")
            if len(fragata_2)==2:
                print(fragata_2 , fragata_2[0], fragata_2[1])
            
                if (fragata_2[0] in self.coord_long and int(fragata_2[1]) in self.coord_lat):
                    if (self.mapa.loc[int(fragata_2[1]),fragata_2[0]]) == ".":
                        self.mapa.loc[int(fragata_2[1]),fragata_2[0]]='F'
                        break
                    else:
                        print('Ya hay un barco en la posición asignada')
                else:
                    print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
            else:
                print("Introducir solo una coordenada del plano.")
        print(self.mapa)

        #Bucle para posición de la fragata_3:
        while True:
            fragata_3 = (input("Fragata 3 de 4 (A-J,0-9): ").upper())
            fragata_3 = fragata_3.split(",")
            if len(fragata_3)==2:
                print(fragata_3 , fragata_3[0], fragata_3[1])
            
                if (fragata_3[0] in self.coord_long and int(fragata_3[1]) in self.coord_lat):
                    if (self.mapa.loc[int(fragata_3[1]),fragata_3[0]]) == ".":
                        self.mapa.loc[int(fragata_3[1]),fragata_3[0]]='F'
                        break
                    else:
                        print('Ya hay un barco en la posición asignada')
                else:
                    print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
            else:
                print("Introducir solo una coordenada del plano.")
        print(self.mapa)

        #Bucle para posición de la fragata_4:
        while True:
            fragata_4 = (input("Fragata 4 de 4 (A-J,0-9): ").upper())
            fragata_4 = fragata_4.split(",")
            if len(fragata_4)==2:
                print(fragata_4 , fragata_4[0], fragata_4[1])
            
                if (fragata_4[0] in self.coord_long and int(fragata_4[1]) in self.coord_lat):
                    if (self.mapa.loc[int(fragata_4[1]),fragata_4[0]]) == ".":
                        self.mapa.loc[int(fragata_4[1]),fragata_4[0]]='F'
                        break
                    else:
                        print('Ya hay un barco en la posición asignada')
                else:
                    print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
            else:
                print("Introducir solo una coordenada del plano.")
        print(self.mapa)
    def posiciones_destructores(self):
        '''
        Establece la posición de tres destructores (2 casillas cada uno). Acepta 3 inputs de estructura (letra,número,letra,número). \n
        Solo permite colocar barcos en disposición vertical u horizontal dentro de los límites del plano establecidos siempre que la casilla no presente otro barco.
        '''
        #Bucle para posicion del destructor_1:
        while True:
            destructor_1 = (input("Destructor 1 de 3 (A-J,0-9,A-J,0-9): ").upper())
            destructor_1 = destructor_1.split(",")
            if len(destructor_1)==4:
                print(destructor_1 , destructor_1[0], destructor_1[1] , destructor_1[2] , destructor_1[3] )
                if (destructor_1[0] in self.coord_long and int(destructor_1[1]) in self.coord_lat) and (destructor_1[2] in self.coord_long and int(destructor_1[3]) in self.coord_lat):
                    if (self.mapa.loc[int(destructor_1[1]),destructor_1[0]] == '.') and (self.mapa.loc[int(destructor_1[3]),destructor_1[2]] == '.'):
                        letra_contigua = (self.coord_long.index(destructor_1[0]) == self.coord_long.index(destructor_1[2])+1) or (self.coord_long.index(destructor_1[0]) == self.coord_long.index(destructor_1[2])-1)
                        numero_contiguo = ((self.coord_lat.index(int(destructor_1[1])) == self.coord_lat.index(int(destructor_1[3]))+1) or (self.coord_lat.index(int(destructor_1[1])) == self.coord_lat.index(int(destructor_1[3]))-1))
                        if (letra_contigua or numero_contiguo) and not(letra_contigua and numero_contiguo):
                            self.mapa.loc[int(destructor_1[1]),destructor_1[0]] = 'D'
                            self.mapa.loc[int(destructor_1[3]),destructor_1[2]] = 'D'
                            break
                        else:
                            print('Las posiciones deben ser contiguas en la horizontal o vertical.')
                    else:
                        print('Ya hay un barco en la posición asignada')
                else:
                    print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
            else:
                print("Se deben introducir dos posiciones en el plano.")
        print(self.mapa)

        #Bucle para posicion del destructor_2:
        while True:
            destructor_2 = (input("Destructor 2 de 3 (A-J,0-9,A-J,0-9): ").upper())
            destructor_2 = destructor_2.split(",")
            if len(destructor_2)==4:
                print(destructor_2 , destructor_2[0], destructor_2[1] , destructor_2[2] , destructor_2[3] )
                if (destructor_2[0] in self.coord_long and int(destructor_2[1]) in self.coord_lat) and (destructor_2[2] in self.coord_long and int(destructor_2[3]) in self.coord_lat):
                    if (self.mapa.loc[int(destructor_2[1]),destructor_2[0]] == '.') and (self.mapa.loc[int(destructor_2[3]),destructor_2[2]] == '.'):
                        letra_contigua = (self.coord_long.index(destructor_2[0]) == self.coord_long.index(destructor_2[2])+1) or (self.coord_long.index(destructor_2[0]) == self.coord_long.index(destructor_2[2])-1)
                        numero_contiguo = ((self.coord_lat.index(int(destructor_2[1])) == self.coord_lat.index(int(destructor_2[3]))+1) or (self.coord_lat.index(int(destructor_2[1])) == self.coord_lat.index(int(destructor_2[3]))-1))
                        if (letra_contigua or numero_contiguo) and not(letra_contigua and numero_contiguo):
                            self.mapa.loc[int(destructor_2[1]),destructor_2[0]] = 'D'
                            self.mapa.loc[int(destructor_2[3]),destructor_2[2]] = 'D'
                            break
                        else:
                            print('Las posiciones deben ser contiguas en la horizontal o vertical.')
                    else:
                        print('Ya hay un barco en la posición asignada')
                else:
                    print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
            else:
                print("Se deben introducir dos posiciones en el plano.")
        print(self.mapa)

        #Bucle para posicion del destructor_3:
        while True:
            destructor_3 = (input("Destructor 3 de 3 (A-J,0-9,A-J,0-9): ").upper())
            destructor_3 = destructor_3.split(",")
            if len(destructor_3)==4:
                print(destructor_3 , destructor_3[0], destructor_3[1] , destructor_3[2] , destructor_3[3] )
                if (destructor_3[0] in self.coord_long and int(destructor_3[1]) in self.coord_lat) and (destructor_3[2] in self.coord_long and int(destructor_3[3]) in self.coord_lat):
                    if (self.mapa.loc[int(destructor_3[1]),destructor_3[0]] == '.') and (self.mapa.loc[int(destructor_3[3]),destructor_3[2]] == '.'):
                        letra_contigua = (self.coord_long.index(destructor_3[0]) == self.coord_long.index(destructor_3[2])+1) or (self.coord_long.index(destructor_3[0]) == self.coord_long.index(destructor_3[2])-1)
                        numero_contiguo = ((self.coord_lat.index(int(destructor_3[1])) == self.coord_lat.index(int(destructor_3[3]))+1) or (self.coord_lat.index(int(destructor_3[1])) == self.coord_lat.index(int(destructor_3[3]))-1))
                        if (letra_contigua or numero_contiguo) and not(letra_contigua and numero_contiguo):
                            self.mapa.loc[int(destructor_3[1]),destructor_3[0]] = 'D'
                            self.mapa.loc[int(destructor_3[3]),destructor_3[2]] = 'D'
                            break
                        else:
                            print('Las posiciones deben ser contiguas en la horizontal o vertical.')
                    else:
                        print('Ya hay un barco en la posición asignada')
                else:
                    print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
            else:
                print("Se deben introducir dos posiciones en el plano.")
        print(self.mapa)
#    def posiciones_acorazados(self):




jugador_t = tablero_defensa_jugador()
print(jugador_t.mapa)

jugador_t.posiciones_destructores()
jugador_t.posiciones_fragatas()
