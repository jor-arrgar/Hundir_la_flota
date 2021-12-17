import pandas as pd
import numpy as np
import random
class tablero_ataque():
    barcos_esloras = [1,1,1,1,2,2,2,3,3,4]  #lista con los barcos y sus esloras para recorrerla con un for y colocarlos en el tablero
    longitud = ['A','B','C','D','E','F','G','H','I','J']
    latitud = [0 ,1 ,2, 3, 4, 5, 6, 7 , 8 , 9]
    mapa_ataque_j = pd.DataFrame(np.full((10,10), '.'), index=longitud, columns=latitud)
    mapa_ataque_m = pd.DataFrame(np.full((10,10), '.'), index=longitud, columns=latitud)
    mapa_defensa_j = pd.DataFrame(np.full((10,10), '.'), index=longitud, columns=latitud)
    mapa_defensa_m = pd.DataFrame(np.full((10,10), '.'), index=longitud, columns=latitud)
    coordenada_ataque = []

    def colocar_barco_j(self):
        print('\nMapa jugador \n', self.mapa_defensa_j)

        #Bucle para posicion del portaviones:
        while True:
            portaviones = (input("Portaviones (A-J,0-9,A-J,0-9,A-J,0-9,A-J,0-9): ").upper())
            portaviones = portaviones.split(",")
            #Comprobacion de longitud correcta de las coordenadas.
            if len(portaviones)==8:
                
                print(portaviones)
                print(portaviones[0] in self.longitud and int(portaviones[1]) in self.latitud)
                print(portaviones[2] in self.longitud and int(portaviones[3]) in self.latitud)
                print(portaviones[4] in self.longitud and int(portaviones[5]) in self.latitud)
                print(portaviones[6] in self.longitud and int(portaviones[7]) in self.latitud)
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

    def colocar_barco_m(self):
       
        #BUCLE A TRAVES DE LAS ESLORAS D
        for barco_len in tablero_ataque.barcos_esloras:

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
    #FUNCION PARA COMPROBAR SI EL BARCO CABE 
    #VARIABLES: LAS ESLORAS DE LOS BARCOS, LA FILA, LA COLUMNA Y LA DIRECCION
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
    #FUNCION PARA COMPROBAR SI YA HAY ALGUN BARCO EN ESA POSICION
    #VARIABLES DE ENTRADA: TABLERO QUE QUEREMOS USAR, FILA SELECCIONADA, COLUMNA, DIRECCION Y LONGITUD DEL BARCO
        if direccion == 'horizontal':
            for i in range(columna, columna + barco_len):
                if self.mapa_defensa_m[fila][i] == 'F' or self.mapa_defensa_m[fila][i] == 'D' or self.mapa_defensa_m[fila][i] == 'A' or self.mapa_defensa_m[fila][i] == 'P':
                    return True
        else:
            for i in range(fila, fila + barco_len):
                if self.mapa_defensa_m[i][columna] == 'F' or self.mapa_defensa_m[i][columna] == 'D' or self.mapa_defensa_m[i][columna] == 'A' or self.mapa_defensa_m[i][columna] == 'P':
                    return True
        return False
        
    
    def ataque_jugador(self):
        print('Empieza el juego')
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
        print('Has atacado la coordenada', x,y)
    def ataque_maquina(self):
        print('Turno de la máquina')
    # while para que el disparo caiga en el tablero,pide coordenadas hasta que introduzca una válida
        long = self.longitud
        lat = self.latitud
        x = random.choice(long)
        y = random.choice(lat)
        self.coordenada_ataque.append(x)
        self.coordenada_ataque.append(y)
        print('La máquina ha atacado la coordenada', x,y)
    def comprobar_ataque_j(self):
        if self.mapa_ataque_j.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] == '~' or self.mapa_ataque_j.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] == 'X':
            print('Ya has disparado a esa casilla')
        elif self.mapa_defensa_m.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] == '.':
            print('Agua')
            self.mapa_ataque_j.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] = '~'
        else:
            print('Tocado')
            self.mapa_ataque_j.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] = 'X'
        print('Tablero jugador','\n',self.mapa_ataque_j,'\n')
    def comprobar_ataque_m(self):
        if self.mapa_ataque_m.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] == '~' or self.mapa_ataque_m.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] == 'X':
            pass
        elif self.mapa_defensa_j.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] == '.':
            print('Agua')
            self.mapa_ataque_m.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] = '~'
        else:
            print('Tocado')
            self.mapa_ataque_m.loc[self.coordenada_ataque[0],self.coordenada_ataque[1]] = 'X'
        print('Tablero máquina','\n',self.mapa_ataque_m,'\n')
jugador = tablero_ataque()
maquina = tablero_ataque()
maquina.colocar_barco_m()
print('\nMapa máquina \n', maquina.mapa_defensa_m)
jugador.colocar_barco_j()
print('\nMapa Ataque Jugador\n', jugador.mapa_ataque_j)
print('\nMapa Ataque Maquina\n', maquina.mapa_ataque_m)
def disparo_jugador():
    while True:
        jugador.coordenada_ataque = []
        jugador.ataque_jugador()
        print(jugador.coordenada_ataque)
        jugador.comprobar_ataque_j()
        print(jugador.coordenada_ataque)
        print(jugador.mapa_ataque_j.loc[jugador.coordenada_ataque[0],jugador.coordenada_ataque[1]])
        if jugador.mapa_ataque_j.loc[jugador.coordenada_ataque[0],jugador.coordenada_ataque[1]] == '~':
            break
        else:
            print('Te vuelve a tocar')
    print('Turno de la máquina')
def disparo_maquina():
    while True:
        maquina.coordenada_ataque = []
        maquina.ataque_maquina()
        print(maquina.coordenada_ataque)
        maquina.comprobar_ataque_m()
        print(maquina.coordenada_ataque)
        print(maquina.mapa_ataque_m.loc[maquina.coordenada_ataque[0],maquina.coordenada_ataque[1]])
        if maquina.mapa_ataque_m.loc[maquina.coordenada_ataque[0],maquina.coordenada_ataque[1]] == '~':
            break
        else:
            print('Te vuelve a tocar')
    print('Turno del jugador')
# juego
disparo_jugador()
disparo_maquina()