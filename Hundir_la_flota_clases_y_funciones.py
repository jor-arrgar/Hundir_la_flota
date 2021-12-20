# Librerías utilizadas para el desarrollo del juego
import pandas as pd
import numpy as np
import random

# Clase tablero ataque. Tablero bidimensional de 10x10, donde jugador y máquina anotan los disparos realizados.
class Tablero(): 
    barcos_esloras = [1,1,1,1,2,2,2,3,3,4]  #lista con los barcos y sus esloras para recorrerla con un for y colocarlos en el tablero
    #Parámetros cardinales.
    longitud = ['A','B','C','D','E','F','G','H','I','J'] 
    latitud = [0 ,1 ,2, 3, 4, 5, 6, 7 , 8 , 9]
    coordenada_ataque = []
    coordenada_central_ataque_orbital = []



    #Generacion de mapas de ataque y defensa de jugador y máquina
    mapa_ataque_j = pd.DataFrame(np.full((10,10), '.'), index=longitud, columns=latitud)
    mapa_ataque_m = pd.DataFrame(np.full((10,10), '.'), index=longitud, columns=latitud)
    mapa_defensa_j = pd.DataFrame(np.full((10,10), '.'), index=longitud, columns=latitud)
    mapa_defensa_m = pd.DataFrame(np.full((10,10), '.'), index=longitud, columns=latitud)
    
    #Contadores
    vida_jugador = 20
    vida_maquina = 20
    contador_ataques_aereos_maquina = 2
    contador_ataques_aereos_jugador = 2


    

    #Método para colocar los barcos del jugador de manera manual.
    def colocar_barco_j(self):
        '''Método para colocar los barcos del jugador, se introducen a través de un input que sólo acepta el formato (A-J,0-9) por casilla. Permite poner un barco portaviones de 4 casillas, 2 acorazados de 3, 3 destructores de 2 y 4 fragatas de 1.'''
        print('\nMapa jugador \n', self.mapa_defensa_j)

        #Bucle para posicion del portaviones:
        while True:
            portaviones = (input("Portaviones (A-J,0-9,A-J,0-9,A-J,0-9,A-J,0-9): ").upper())
            portaviones = portaviones.split(",")
            #Comprobacion de longitud correcta de las coordenadas.
            if len(portaviones)==8:
                
                #Comprobación de que cada elemento se ha introducido en el orden correcto y está dentro de los rangos establecidos.
                #Incluye un 'try' para evitar que el codigo se rompa si se intenta generar un integer de una letra.
                try:
                    if (portaviones[0] in self.longitud and int(portaviones[1]) in self.latitud) and (portaviones[2] in self.longitud and int(portaviones[3]) in self.latitud) and (portaviones[4] in self.longitud and int(portaviones[5]) in self.latitud) and (portaviones[6] in self.longitud and int(portaviones[7]) in self.latitud):
                        
                        #Comprobacion de que las coordenadas elegidas están disponibles para colocar un barco.
                        if (self.mapa_defensa_j.loc[portaviones[0],int(portaviones[1])] == '.') and (self.mapa_defensa_j.loc[portaviones[2],int(portaviones[3])] == '.') and (self.mapa_defensa_j.loc[portaviones[4],int(portaviones[5])] == '.'):
                            
                            #Comprobación de que las posiciones escogidas son contiguas en la vertical o en la horizontal.
                            letra12_contiguas = ((self.longitud.index(portaviones[0]) == self.longitud.index(portaviones[2])+1) or (self.longitud.index(portaviones[0]) == self.longitud.index(portaviones[2])-1)) 
                            letra23_contiguas = ((self.longitud.index(portaviones[2]) == self.longitud.index(portaviones[4])+1) or (self.longitud.index(portaviones[2]) == self.longitud.index(portaviones[4])-1))
                            letra34_contiguas = ((self.longitud.index(portaviones[4]) == self.longitud.index(portaviones[6])+1) or (self.longitud.index(portaviones[4]) == self.longitud.index(portaviones[6])-1))
                            
                            numeros12_contiguos = ((self.latitud.index(int(portaviones[1])) == self.latitud.index(int(portaviones[3]))+1) or (self.latitud.index(int(portaviones[1])) == self.latitud.index(int(portaviones[3]))-1)) 
                            numeros23_contiguos = ((self.latitud.index(int(portaviones[3])) == self.latitud.index(int(portaviones[5]))+1) or (self.latitud.index(int(portaviones[3])) == self.latitud.index(int(portaviones[5]))-1))
                            numeros34_contiguos = ((self.latitud.index(int(portaviones[5])) == self.latitud.index(int(portaviones[7]))+1) or (self.latitud.index(int(portaviones[5])) == self.latitud.index(int(portaviones[7]))-1))
                            
                            letras_contiguas = letra12_contiguas and letra23_contiguas and letra34_contiguas
                            numeros_contiguos = numeros12_contiguos and numeros23_contiguos and numeros34_contiguos
                            
                            #Las siguientes comprobaciones incluyen que no se permitan posiciones en diagonal.
                            if letras_contiguas and (portaviones[1] == portaviones[3] == portaviones[5] == portaviones[7]):
                                #Colocar varco en la horizontal
                                self.mapa_defensa_j.loc[portaviones[0],int(portaviones[1])] = 'P'
                              
                                self.mapa_defensa_j.loc[portaviones[2],int(portaviones[3])] = 'P'
                         
                                self.mapa_defensa_j.loc[portaviones[4],int(portaviones[5])] = 'P'
                        
                                self.mapa_defensa_j.loc[portaviones[6],int(portaviones[7])] = 'P'
                          
                                break
                            elif numeros_contiguos and (portaviones[0] == portaviones[2] == portaviones[4] == portaviones[6]):
                                #Colocar barco en la vertical
                                self.mapa_defensa_j.loc[portaviones[0],int(portaviones[1])] = 'P'
                            
                                self.mapa_defensa_j.loc[portaviones[2],int(portaviones[3])] = 'P'
                       
                                self.mapa_defensa_j.loc[portaviones[4],int(portaviones[5])] = 'P'
                               
                                self.mapa_defensa_j.loc[portaviones[6],int(portaviones[7])] = 'P'
                              
                                break
                            else:
                                print('Las posiciones deben ser contiguas en la horizontal o vertical.')
                        else:
                            print('Ya hay un barco en la posición asignada')
                    else:
                        print("El único formato válido es 'letra,número' dentro de los rangos establecidos k.")
                except:
                    print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
            else:
                print("Se deben introducir cuatro posiciones en el plano.")
        print(self.mapa_defensa_j)

        #Bucle para posicion de los acorazados:
        for i in range(1,3):
            while True:
                acorazado_i = (input("Acorazado " + str(i) + " de 2 (A-J,0-9,A-J,0-9,A-J,0-9): ").upper())
                acorazado_i = acorazado_i.split(",")
                #Comprobacion de longitud correcta de las coordenadas.
                if len(acorazado_i)==6:
                    
                    #Comprobación de que cada elemento se ha introducido en el orden correcto y está dentro de los rangos establecidos.
                    #Incluye un 'try' para evitar que el codigo se rompa si se intenta generar un integer de una letra.
                    try:
                        if (acorazado_i[0] in self.longitud and int(acorazado_i[1]) in self.latitud) and (acorazado_i[2] in self.longitud and int(acorazado_i[3]) in self.latitud) and (acorazado_i[4] in self.longitud and int(acorazado_i[5]) in self.latitud):
                            
                            #Comprobacion de que las coordenadas elegidas están disponibles para colocar un barco.
                            if (self.mapa_defensa_j.loc[acorazado_i[0],int(acorazado_i[1])] == '.') and (self.mapa_defensa_j.loc[acorazado_i[2],int(acorazado_i[3])] == '.') and (self.mapa_defensa_j.loc[acorazado_i[4],int(acorazado_i[5])] == '.'):
                                
                                #Comprobación de que las posiciones escogidas son contiguas en la vertical o en la horizontal.
                                letra12_contiguas = ((self.longitud.index(acorazado_i[0]) == self.longitud.index(acorazado_i[2])+1) or (self.longitud.index(acorazado_i[0]) == self.longitud.index(acorazado_i[2])-1)) 
                                letra23_contiguas = ((self.longitud.index(acorazado_i[2]) == self.longitud.index(acorazado_i[4])+1) or (self.longitud.index(acorazado_i[2]) == self.longitud.index(acorazado_i[4])-1))
                                numeros12_contiguos = ((self.latitud.index(int(acorazado_i[1])) == self.latitud.index(int(acorazado_i[3]))+1) or (self.latitud.index(int(acorazado_i[1])) == self.latitud.index(int(acorazado_i[3]))-1)) 
                                numeros23_contiguos = ((self.latitud.index(int(acorazado_i[3])) == self.latitud.index(int(acorazado_i[5]))+1) or (self.latitud.index(int(acorazado_i[3])) == self.latitud.index(int(acorazado_i[5]))-1))
                                
                                letras_contiguas = letra12_contiguas and letra23_contiguas
                                numeros_contiguos = numeros12_contiguos and numeros23_contiguos
                                
                                #Las siguientes comprobaciones incluyen que no se permitan posiciones en diagonal.
                                if letras_contiguas and (acorazado_i[1] == acorazado_i[3] == acorazado_i[5]):
                                    #Colocación del barco en horizontal
                                    self.mapa_defensa_j.loc[acorazado_i[0],int(acorazado_i[1])] = 'A'
                                  
                                    self.mapa_defensa_j.loc[acorazado_i[2],int(acorazado_i[3])] = 'A'
                                  
                                    self.mapa_defensa_j.loc[acorazado_i[4],int(acorazado_i[5])] = 'A'
                                    
                                    break
                                elif numeros_contiguos and (acorazado_i[0] == acorazado_i[2] == acorazado_i[4]):
                                    #Colocación del barco en vertical
                                    self.mapa_defensa_j.loc[acorazado_i[0],int(acorazado_i[1])] = 'A'
                                   
                                    self.mapa_defensa_j.loc[acorazado_i[2],int(acorazado_i[3])] = 'A'
                                    
                                    self.mapa_defensa_j.loc[acorazado_i[4],int(acorazado_i[5])] = 'A'
                                    
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
            print(self.mapa_defensa_j)

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
                        if (destructor_i[0] in self.longitud and int(destructor_i[1]) in self.latitud) and (destructor_i[2] in self.longitud and int(destructor_i[3]) in self.latitud):
                            
                            #Comprobacion de que las coordenadas elegidas están disponibles para colocar un barco.
                            if (self.mapa_defensa_j.loc[destructor_i[0],int(destructor_i[1])] == '.') and (self.mapa_defensa_j.loc[destructor_i[2],int(destructor_i[3])] == '.'):
                                
                                #Comprobación de que las posiciones escogidas son contiguas en la vertical o en la horizontal.
                                letra_contigua = (self.longitud.index(destructor_i[0]) == self.longitud.index(destructor_i[2])+1) or (self.longitud.index(destructor_i[0]) == self.longitud.index(destructor_i[2])-1)
                                numero_contiguo = ((self.latitud.index(int(destructor_i[1])) == self.latitud.index(int(destructor_i[3]))+1) or (self.latitud.index(int(destructor_i[1])) == self.latitud.index(int(destructor_i[3]))-1))
                                
                                #Las siguientes comprobaciones incluyen que no se permitan posiciones en diagonal.
                                if (letra_contigua or numero_contiguo) and not(letra_contigua and numero_contiguo):
                                    self.mapa_defensa_j.loc[destructor_i[0],int(destructor_i[1])] = 'D'
                                    
                                    self.mapa_defensa_j.loc[destructor_i[2],int(destructor_i[3])] = 'D'
                                  
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
            print(self.mapa_defensa_j)

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
                        if (fragata_i[0] in self.longitud and int(fragata_i[1]) in self.latitud):

                            #Comprobacion de que las coordenadas elegidas están disponibles para colocar un barco.
                            if (self.mapa_defensa_j.loc[fragata_i[0],int(fragata_i[1])]) == ".":

                                #Colocación del barco
                                self.mapa_defensa_j.loc[fragata_i[0],int(fragata_i[1])]='F'
                              
                                break
                            else:
                                print('Ya hay un barco en la posición asignada')
                        else:
                            print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
                    except:
                        print("El único formato válido es 'letra,número' dentro de los rangos establecidos.")
                else:
                    print("Introducir solo una coordenada del plano.")
            print(self.mapa_defensa_j)

 
                                
                        else:
                            for i in range(fila, fila + barco_len):
                                if barco_len == 1:
                                    self.mapa_defensa_j[i][columna] = 'F'
                                   
                                elif barco_len == 2:
                                    self.mapa_defensa_j[i][columna] = 'D'
                                 
                                elif barco_len == 3:
                                    self.mapa_defensa_j[i][columna] = 'A'
                                   
                                elif barco_len == 4:
                                    self.mapa_defensa_j[i][columna] = 'P'
                                  
                        break

    def colocar_barco_m(self):
        '''Método aleatorio para posicionar los barcos de la máquina. Permite colocar 1 portaviones, 2 acorazados, 3 destructories y 4 fragatas'''
       
        #BUCLE A TRAVES DE LAS ESLORAS D
        for barco_len in self.barcos_esloras:

            #HACEMOS UN BUCLE PARA COMPROBAR QUE EL BARCO CABE Y NO PISA A OTRO BARCO. SI SE CUMPLEN, COLOCAMOS
            while True:
                direccion, fila, columna = random.choice(['horizontal', 'vertical']), random.randint(0,9), random.randint(0,9)

                #LLAMAMOS A LA FUNCION BARCO_CABE PARA COMPROBAR SI CABE EL BARCO
                if self.barco_cabe(barco_len, fila, columna, direccion): 

                    #LLAMAMOS A LA FUNCION BARCO_SUPERPUESTO
                    if self.barco_superpuesto(fila, columna, direccion, barco_len) == False: 

                        #COLOCAMOS BARCO, CADA POSICION SE REPRESENTA CON LA INICIAL DE CADA TIPO DE BARCO:
                        #F:FRAGATA, D:DESTRUCTOR, A:ACORAZADO, P:PORTAAVIONES
                        if direccion == 'horizontal':
                            for i in range(columna, columna + barco_len):
                                if barco_len == 1:
                                    self.mapa_defensa_m[fila][i] = 'F'
                                    
                                elif barco_len == 2:
                                    self.mapa_defensa_m[fila][i] = 'D'
                                  
                                elif barco_len == 3:
                                    self.mapa_defensa_m[fila][i] = 'A'
                                
                                elif barco_len == 4:
                                    self.mapa_defensa_m[fila][i] = 'P'
                                 
                        else:
                            for i in range(fila, fila + barco_len):
                                if barco_len == 1:
                                    self.mapa_defensa_m[i][columna] = 'F'
                                  
                                elif barco_len == 2:
                                    self.mapa_defensa_m[i][columna] = 'D'
                                 
                                elif barco_len == 3:
                                    self.mapa_defensa_m[i][columna] = 'A'
                                    
                                elif barco_len == 4:
                                    self.mapa_defensa_m[i][columna] = 'P'
                               
                        break
       
    def barco_cabe(self, barco_len, fila, columna, direccion):
        '''FUNCION PARA COMPROBAR SI LOS BARCOS DE LA MÁQUINA CABEN EN EL PLANO
        VARIABLES: LAS ESLORAS DE LOS BARCOS, LA FILA, LA COLUMNA Y LA DIRECCION'''
        if direccion == 'horizontal':
            if columna + barco_len >= 10:
                return False
            else:
                return True
        else:
            if fila + barco_len >= 10:
                return False
            else:
                return True

    def barco_superpuesto(self, fila, columna, direccion, barco_len):
        '''FUNCION PARA COMPROBAR SI YA HAY ALGUN BARCO EN ESA POSICION
        VARIABLES DE ENTRADA: TABLERO QUE QUEREMOS USAR, FILA SELECCIONADA, COLUMNA, DIRECCION Y LONGITUD DEL BARCO'''
        if direccion == 'horizontal':
            for i in range(columna, columna + barco_len):
                if (self.mapa_defensa_m[fila][i] == 'F') or (self.mapa_defensa_m[fila][i] == 'D') or (self.mapa_defensa_m[fila][i] == 'A') or (self.mapa_defensa_m[fila][i] == 'P'):
                    return True
        else:
            for i in range(fila, fila + barco_len):
                if (self.mapa_defensa_m[i][columna] == 'F') or (self.mapa_defensa_m[i][columna] == 'D') or (self.mapa_defensa_m[i][columna] == 'A') or (self.mapa_defensa_m[i][columna] == 'P'):
                    return True
        return False
           
    def ataque_jugador(self):
        '''MÉTODO PARA GENERAR UNA COORDENADA DE ATAQUE POR PARTE DEL JUGADOR'''
        print("Turno del jugador.")
        # while para que el disparo caiga en el tablero,pide coordenadas hasta que introduzca una válida
        while True:
            x = input('Dispara a fila: ').upper()
            if x in self.longitud:
                break
            else:
                print('Coordenada incorrecta')
        while True:
            y = input('Dispara a columna: ')
            try:
                y = int(y)
                if y in self.latitud:
                    break
                else:
                    print('Coordenada incorrecta')
            except:
                print('Valor introducido incorrecto')
        self.coordenada_ataque.append(x)
        self.coordenada_ataque.append(y)
    
    #Método para que la máquina ataque una coordenada, lo hace de manera aleatoria.
    def ataque_maquina(self):
        '''MÉTODO PARA GENERAR UNA COORDENADA DE ATAQUE POR PARTE DE LA MÁQUINA'''
        barcos_tocados = []
        sin_usar = []

        #PENSAR, en caso que la máquina acierte en un barco, blucle para que la máquina siga atacando esa posición, buscando posiciones contiguas para hundir el barco.
        pensar = random.choice([0 , 1 , 2])
        if pensar <= 1: 
            for i in self.longitud:
                for j in self.latitud:
                    if self.mapa_ataque_m.loc[i , j] == 'X':
                        barcos_tocados.append([i , j])
                    else:
                        pass
            
            if len(barcos_tocados) > 0:          
                
                while True:
                    direccion = random.choice(['derecha' , 'izquierda' , 'arriba' , 'abajo'])
                    barco_tocado = random.choice(barcos_tocados)
                    self.coordenada_ataque = []
                    print(barco_tocado)
                    if (direccion == 'abajo') and (self.longitud.index(barco_tocado[0]) + 1 <= 9):
                        self.coordenada_ataque.append(self.longitud[self.longitud.index(barco_tocado[0]) + 1])
                        self.coordenada_ataque.append(barco_tocado[1])
                        break
                    elif  (direccion == 'arriba') and (0 <= self.longitud.index(barco_tocado[0]) - 1):
                        self.coordenada_ataque.append(self.longitud[self.longitud.index(barco_tocado[0]) - 1])
                        self.coordenada_ataque.append(barco_tocado[1])
                        break
                    elif (direccion == 'derecha') and (barco_tocado[1] + 1 <= 9):
                        self.coordenada_ataque.append(barco_tocado[0])
                        self.coordenada_ataque.append(barco_tocado[1] + 1)
                        break
                    elif (direccion == 'izquierda') and (0 <= barco_tocado[1] -1):
                        self.coordenada_ataque.append(barco_tocado[0])
                        self.coordenada_ataque.append(barco_tocado[1] - 1)
                        break
                    else:
                        pass
                
            else:
                self.coordenada_ataque = []
                x = random.choice(self.longitud)
                y = random.choice(self.latitud)
                self.coordenada_ataque.append(x)
                self.coordenada_ataque.append(y)
    
        else:
            self.coordenada_ataque = []
            for i in self.longitud:
                for j in self.latitud:
                    if self.mapa_ataque_m.loc[i , j] == '.':
                        sin_usar.append([i , j])
                    else:
                        pass
            self.coordenada_ataque = random.choice(sin_usar)
    # Comprobación de dónde cae el disparo del jugador. Comprueba el disparo en el mapa de defensa y muestra el disparo en el mapa de ataque.
    def comprobar_ataque_j(self):
        '''MÉTODO QUE COMPRUEBA SI EL ATAQUE DEL JUGADOR HA SIDO REPETIDO, HA CAIDO EN AGUA, O EN POSICIÓN DE BARCO'''
        
        if self.mapa_ataque_j.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] == '~' or self.mapa_ataque_j.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] == 'X':
            print('Ya has disparado a esa casilla')
         
        elif self.mapa_defensa_m.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] == '.':
            print('Has atacado la coordenada', self.coordenada_ataque[0] , self.coordenada_ataque[1])
            print('Agua')
            self.mapa_ataque_j.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] = '~'
            self.mapa_defensa_m.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] = 'X'
        else:
            print('Has atacado la coordenada', self.coordenada_ataque[0] , self.coordenada_ataque[1])
            print('Tocado')
            self.mapa_ataque_j.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] = 'X'
            self.mapa_defensa_m.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] = 'X'
            
         #En cada disparo realizado se muestra el tablero de ataque del jugador   
        print('Tablero jugador','\n',self.mapa_ataque_j,'\n')

    # Comprobación de dónde cae el disparo de la máquina. Comprueba el disparo en el mapa de defensa y muestra el disparo en el mapa de ataque. 
    def comprobar_ataque_m(self):
        '''MÉTODO QUE COMPRUEBA SI EL ATAQUE DE LA MÁQUINA HA SIDO REPETIDO, HA CAIDO EN AGUA, O EN POSICIÓN DE BARCO'''

        while True:
            if self.mapa_ataque_m.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] == '~' or self.mapa_ataque_m.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] == 'X':
                self.ataque_maquina()
            elif self.mapa_defensa_j.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] == '.':
                print("La máquina ha atacado a la coordenada " , self.coordenada_ataque[0] , self.coordenada_ataque[1])
                print('Agua')
                self.mapa_ataque_m.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] = '~'
                self.mapa_defensa_j.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] = 'X'
                break
            else:
                print("La máquina ha atacado a la coordenada " , self.coordenada_ataque[0] , self.coordenada_ataque[1])
                print('Tocado')
                self.mapa_ataque_m.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] = 'X'
                self.mapa_defensa_j.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] = 'X'
                
                break
            
        #En cada disparo realizado se muestra el tablero de ataque del jugador    

    def ataque_aereo_m(self):
        '''MÉTODO QUE GENERA UN ATAQUE MÚLTIPLE SOBRE UNA FILA O COLUMNA COMPLETAS POR PARTE DE LA MÁQUINA'''
        #metodo que genera un ataque conjunto a toda una fila o a toda una columna, simunaldo el paso de un escuadrón de bombarderos, coordenadas elegidas por la máquina aleatorias 
        plano = ['latitud' , 'longitud']
        ataque_aereo = random.choice(plano)
        if ataque_aereo == 'latitud':
            ataque_aereo_vertical = random.choice(self.latitud)
            for casilla_horizontal in self.longitud:
                if (self.mapa_defensa_j.loc[casilla_horizontal, ataque_aereo_vertical] != '.') and (self.mapa_defensa_j.loc[casilla_horizontal, ataque_aereo_vertical]) != 'X':
                    self.mapa_defensa_j.loc[casilla_horizontal, ataque_aereo_vertical] = 'X'
                    self.mapa_ataque_m.loc[casilla_horizontal , ataque_aereo_vertical] = 'X'
                    self.vida_jugador -= 1
                    print('Tocado en coordenadas ' , casilla_horizontal , ataque_aereo_vertical)
                    
                elif self.mapa_defensa_j.loc[casilla_horizontal, ataque_aereo_vertical] == 'X':
                    pass
                else:
                    self.mapa_defensa_j.loc[casilla_horizontal, ataque_aereo_vertical] = 'X'
                    self.mapa_ataque_m.loc[casilla_horizontal , ataque_aereo_vertical] = '~'
                    print("Agua en coordenadas " , casilla_horizontal , ataque_aereo_vertical)
     
        else:
            ataque_aereo_horizontal = random.choice(self.longitud)
            for casilla_vertical in self.latitud:
                if (self.mapa_defensa_j.loc[ataque_aereo_horizontal , casilla_vertical] != '.') and (self.mapa_defensa_j.loc[ataque_aereo_horizontal , casilla_vertical] != 'X'):
                    self.mapa_defensa_j.loc[ataque_aereo_horizontal , casilla_vertical] = 'X'
                    self.mapa_ataque_m.loc[ataque_aereo_horizontal , casilla_vertical] = 'X'
                    self.vida_jugador -= 1
                    print ("Tocado en coordenadas " , ataque_aereo_horizontal , casilla_vertical)
                elif self.mapa_defensa_j.loc[ataque_aereo_horizontal , casilla_vertical] == 'X':
                    pass
                else:
                    self.mapa_defensa_j.loc[ataque_aereo_horizontal , casilla_vertical] = 'X'
                    self.mapa_ataque_m.loc[ataque_aereo_horizontal , casilla_vertical] = '~'
                    print("Agua en coordenadas " , ataque_aereo_horizontal , casilla_vertical)

    #metodo que genera un ataque conjunto a toda una fila o a toda una columna, simunaldo el paso de un escuadrón de bombarderos, coredenadas elegidas por el jugador
    def ataque_aereo_j(self):
        '''MÉTODO QUE GENERA UN ATAQUE MÚLTIPLE SOBRE UNA FILA O COLUMNA COMPLETAS POR PARTE DEL JUGADOR'''
        while True:
            ataque_aereo = input('Elija la dirección del ataque aéreo (fila , columna o "pasar"): ')
            try:
                ataque_aereo = int(ataque_aereo)
                if ataque_aereo in self.latitud:
                    ataque_aereo_vertical = ataque_aereo
                    for casilla_horizontal in self.longitud:
                        if (self.mapa_defensa_m.loc[casilla_horizontal, ataque_aereo_vertical] != '.') and (self.mapa_defensa_j.loc[casilla_horizontal, ataque_aereo_vertical]) != 'X':
                            self.mapa_defensa_m.loc[casilla_horizontal, ataque_aereo_vertical] = 'X'
                            self.mapa_ataque_j.loc[casilla_horizontal , ataque_aereo_vertical] = 'X'
                            self.vida_maquina -= 1
                            
                                        
                            print('Tocado en coordenadas ' , casilla_horizontal , ataque_aereo_vertical)
                            
                        elif self.mapa_defensa_m.loc[casilla_horizontal, ataque_aereo_vertical] == 'X':
                            pass
                        else:
                            self.mapa_defensa_m.loc[casilla_horizontal, ataque_aereo_vertical] = 'X'
                            self.mapa_ataque_j.loc[casilla_horizontal , ataque_aereo_vertical] = '~'
                            print("Agua en coordenadas " , casilla_horizontal , ataque_aereo_vertical)
                    break
                else:
                    print("Valor de coordenada vertical no válido")
            except:
                ataque_aereo = ataque_aereo.upper()
                if ataque_aereo in self.longitud:
                    ataque_aereo_horizontal = ataque_aereo
                    for casilla_vertical in self.latitud:
                        if (self.mapa_defensa_m.loc[ataque_aereo_horizontal , casilla_vertical] != '.') and (self.mapa_defensa_j.loc[ataque_aereo_horizontal , casilla_vertical] != 'X'):
                            self.mapa_defensa_m.loc[ataque_aereo_horizontal , casilla_vertical] = 'X'
                            self.mapa_ataque_j.loc[ataque_aereo_horizontal , casilla_vertical] = 'X'
                            print ("Tocado en coordenadas " , ataque_aereo_horizontal , casilla_vertical)
                        elif self.mapa_defensa_m.loc[ataque_aereo_horizontal , casilla_vertical] == 'X':
                            pass
                        else:
                            self.mapa_defensa_m.loc[ataque_aereo_horizontal , casilla_vertical] = 'X'
                            self.mapa_ataque_j.loc[ataque_aereo_horizontal , casilla_vertical] = '~'
                            print("Agua en coordenadas " , ataque_aereo_horizontal , casilla_vertical)
                    break
                elif ataque_aereo.upper() == 'PASAR':
                    break
                else:
                    print("Valor de coordenada horizontal no válida.")

    def ataque_orbital(self):
        '''MÉTODO QUE GENERA UN ATAQUE DE 3X3 SOBRE EL TABLERO DEL JUGADOR'''
        #solo lo puede ejecutar la máquina, ataque del nivel 3. La máquina ataca una posición, y todas las de su alrededor en un solo disparo.
        coord = [1, 2 , 3 , 4 , 5, 6, 7, 8]
        x = random.choice(coord)
        y = random.choice(coord)
        self.coordenada_central_ataque_orbital.append(x)
        self.coordenada_central_ataque_orbital.append(y)
        for perimetro in [(-1 , -1) , (-1, 0) , (-1 , 1) , (0, -1) , (0 , 0) , (0 , 1) , (1 , -1) , (1 , 0) , (1 , 1)]:
            coordenada_ataque_orbital = self.coordenada_central_ataque_orbital[0] + perimetro[0]  , self.coordenada_central_ataque_orbital[1] + perimetro[1]
            if self.mapa_defensa_j.iloc[coordenada_ataque_orbital] == '.':
                print("Agua en coordenadas " , coordenada_ataque_orbital)
                self.mapa_defensa_j.iloc[coordenada_ataque_orbital] = 'X'
                self.mapa_ataque_m.iloc[coordenada_ataque_orbital] = '~'
            elif self.mapa_defensa_j.iloc[coordenada_ataque_orbital] == 'X':
                pass
            else:
                print("Tocado en coordenadas " , coordenada_ataque_orbital)
                self.mapa_defensa_j.iloc[coordenada_ataque_orbital] = 'X'
                self.mapa_ataque_m.iloc[coordenada_ataque_orbital] = 'X'
                self.vida_jugador -= 1
                





                



#Establecimiento de objetos 'tablero' y aplicación de los metodos de colocacion de barcos
jugador = Tablero()
maquina = Tablero()


#Definicion de funciones de juego

def disparo_jugador():
    '''FUNCIÓN QUE PERMITE DISPARAR, Y SI EL JUGADOR ACIERTA LE VUELVE A TOCAR'''
    while True:
        # Bucle para comprobación del disparo del jugador. En caso de acertar,te vuelve a tocar. 
        jugador.coordenada_ataque = []
        jugador.ataque_jugador()
        jugador.comprobar_ataque_j()
        if jugador.mapa_ataque_j.loc[jugador.coordenada_ataque[0],jugador.coordenada_ataque[1]] == '~':
            break
        else:
            maquina.vida_maquina -= 1
            print('Te vuelve a tocar')
    print('Turno de la máquina')

def disparo_maquina():
    '''FUNCIÓN QUE PERMITE DISPARAR, Y SI LA MÁQUINA ACIERTA LE VUELVE A TOCAR'''
    print("Turno de la maquina")
    # Bucle para comprobación del disparo de la máquina. En caso de acertar,te vuelve a tocar. 
    while True:
        maquina.coordenada_ataque = []
        maquina.ataque_maquina()
        print(maquina.mapa_defensa_j.loc[maquina.coordenada_ataque[0],maquina.coordenada_ataque[1]])
        maquina.comprobar_ataque_m()
        if maquina.mapa_ataque_m.loc[maquina.coordenada_ataque[0],maquina.coordenada_ataque[1]] == '~':
            break
        else:
            jugador.vida_jugador -= 1
            print('Te vuelve a tocar')
    print('Turno del jugador')

def ataque_aereo_maquina():
    '''FUNCION QUE PERMITE EJECUTAR UN ATAQUE AÉREO A LA MÁQUINA EN BASE A UNA PROBABILIDAD DETERMINADA'''
    if maquina.contador_ataques_aereos_maquina > 0:
        ejecucion = random.choice([0 , 1 , 2 , 3])
        if ejecucion == 0:
            print("La máquina va a ejecutar un ataque aéreo")
            maquina.ataque_aereo_m()
            print(jugador.mapa_defensa_j)
            maquina.contador_ataques_aereos_maquina -= 1
        else:
            print('La maquina NO ejecuta un ataque aereo')
    else:
        print("A la maquina no le quedan ataques aereos")

def ataque_aereo_jugador():
    '''FUNCION QUE PERMITE EJECUTAR UN ATAQUE AÉREO AL JUGADOR CUANDO LE INTERESE'''
    if jugador.contador_ataques_aereos_jugador > 0:
        jugador.ataque_aereo_j()
        print(jugador.mapa_ataque_j)
        jugador.contador_ataques_aereos_jugador -= 1
    else:
        print('Al jugador no le quedan ataques aereos')
# Ataque orbital. Se le avisa al jugador del próximo ataque. El jugador tiene opción a defenserse.
def ataque_orbital():
    '''FUNCION QUE PERMITE A LA MAQUINA REALIAR UN ATAQUE ORBITAL, Y AL JUGADOR LA POSIBLIDAD DE DEFENDERSE'''
    print("La flota enemiga está preparando un ataque satelital.")
    maquina.coordenadas_ataque_orbital = []
    ejecucion = random.choice(list(range(0,6)))
    # Hay 7 posibilidades, la máquina elige aleatoriamente una. Si es 4 o mayor, realiza el ataque. Si es 3, el jugador tiene posibilidad de defenderse. Si es inferior a 3, no realiza el ataque.
    if ejecucion > 3:
        maquina.ataque_orbital()
        print("La flota enemiga va a lanzar un ataque orbital sobre las coordenadas %s, ¡PREPARATE PARA EL IMPACTO!" % maquina.coordenadas_ataque_orbital)
    elif ejecucion == 3:
        defensa = random.choice(list(range(0,5)))
        #Bucle para opción a defenderse del artaque orbital.
        while True:
            oportunidad = input("Elije un numero entre 0 y 5 (incluidos): ")
            try:
                oportunidad = int(oportunidad)
                if oportunidad in list(range(0,5)):
                    if oportunidad == defensa:
                        print("Tu división de guerra electronica ha detenido el ataque orbital.")
                        break
                    else:
                        maquina.ataque_orbital()
                        print("La flota enemiga va a lanzar un ataque orbital sobre las coordenadas %s, ¡PREPARATE PARA EL IMPACTO!" % maquina.coordenadas_ataque_orbital)
                        break
                else:
                    print("Valor introducido fuera de rango")
            except:
                print("Carácter introducido no válido, solo se permiten caracteres numéricos.")
    else:
        print("La flota enemiga no ha conseguido lanzar el ataque orbital.")

def reset():
    '''RESETEA LOS PARAMETROS DE LOS MAPAS Y LOS CONTADORES'''
    while True: 
        jugador.ataque_jugador = jugador.ataque_jugador.reset()
        jugador.defensa_jugador = jugador.defensa_jugador.reset()
        maquina.ataque_maquina = maquina.ataque_maquina.reset()
        maquina.defensa_maquina = maquina.defensa_maquina.reset()
        maquina.contador_ataques_aereos_maquina = 2
        jugador.contador_ataques_aereos_jugador = 2
        jugador.vida_jugador = 20
        maquina.vida_maquina = 20

def colocar_barcos()
    maquina.colocar_barco_m()
    jugador.colocar_barco_j()