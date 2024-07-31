print("Almacen estado incial")
almacen = [ ['1','#','0', '3'],
            ['0','#','0', '0'],
            ['2','0','R', '0'],
            ['0','0','0', '0'],
        ]
print(almacen[0])
print(almacen[1])
print(almacen[2])
print(almacen[3])

print("Almacen Objetivo")
almacenObjetivo = [ 
            ['0','#','0', '0'],
            ['0','#','0', '0'],
            ['0','0','0', '0'],
            ['0','3','2', '1'],
        ]
print(almacenObjetivo[0])
print(almacenObjetivo[1])
print(almacenObjetivo[2])
print(almacenObjetivo[3])

print("Encontrar posiciones de Robot y M1...Mn")
posicion_R = [-1,-1]
for i, fila in enumerate(almacen):
    for j, valor in enumerate(fila):
        if valor == 'R':
            posicion_R[0] = j
            posicion_R[1] = i
            break
    if posicion_R[0]!= -1 :
        break
print("Posicion inicial de robot ", posicion_R)

numInventarios = 3
posicion_M = [[-1,-1],
              [-1,-1],
              [-1,-1]
             ]

for x in range(numInventarios):
    for i, fila in enumerate(almacen):
        for j, valor in enumerate(fila):
            if valor == str(x+1):
                posicion_M[x][0] = i
                posicion_M[x][1] = j
                break
        if posicion_M[x][0]!= -1 :
            break
print("Posicion de inventarios")        
for x in range(numInventarios):
    print("M",x+1,":",posicion_M[x])

posicion_M_Objetivo= [[-1,-1],
              [-1,-1],
              [-1,-1]
             ]

for x in range(numInventarios):
    for i, fila in enumerate(almacenObjetivo):
        for j, valor in enumerate(fila):
            if valor == str(x+1):
                posicion_M_Objetivo[x][0] = i
                posicion_M_Objetivo[x][1] = j
                break
        if posicion_M_Objetivo[x][0]!= -1 :
            break
print("Posicion de inventarios")        
for x in range(numInventarios):
    print("M",x+1,":",posicion_M_Objetivo[x])

def distanciaManhattan(x,y,g=0):
    if g!=0:
        f = abs(x[0]-y[0]) + abs(x[1]-y[1])
        return f
    else:
        f = abs(x[0]-y[0]) + abs(x[1]-y[1])
        return f+g


def acomodarAlmacen(almacenActual,posicionRobot, tamanioMatriz, m):
    print("La posición actual del robot es:", posicionRobot[0], posicionRobot[1])
    print("Considerando que puede desplazarce unicamente de forma vertical y horizontal las posibles opciones son las siguientes")
    siguientePosicion = [-1,-1]
    minimo = 0
    print("Estatus de almacen previo a iniciar")
    print(almacenActual[0])
    print(almacenActual[1])        
    print(almacenActual[2])
    print(almacenActual[3])
    # El rango utilizado es 4 porque es el numero maximo de opciones que puede tener el robot en todos los escenarios posibles
    while siguientePosicion != posicion_M[m]:
        if(posicionRobot[1]+1 >= 0 and posicionRobot[1]+1 < tamanioMatriz and almacenActual[posicionRobot[0]][posicionRobot[1]+1] != "#"):
            print("Se puede mover una posición a derecha")
            print("Posición con cordenadas: ", posicionRobot[0], posicionRobot[1]+1)  
            distanciaAbajo = distanciaManhattan([ posicionRobot[0], posicionRobot[1]+1], posicion_M[m])
            print(distanciaAbajo)
            minimo = distanciaAbajo
            siguientePosicion = [ posicionRobot[0], posicionRobot[1]+1]

        if(posicionRobot[1]-1 >= 0 and posicionRobot[1]-1 < tamanioMatriz and almacenActual[posicionRobot[0]][posicionRobot[1]-1] != "#"):
            print("Se puede mover una posición izquierda")
            print("Posición con cordenadas: ", posicionRobot[0], posicionRobot[1]-1)  
            distanciaArriba = distanciaManhattan([ posicionRobot[0], posicionRobot[1]-1], posicion_M[m])
            print(distanciaArriba)
            if(minimo> distanciaArriba):
                minimo = distanciaArriba
                siguientePosicion = [ posicionRobot[0], posicionRobot[1]-1]
        if(posicionRobot[0]+1 >= 0 and posicionRobot[0]+1 < tamanioMatriz and almacenActual[posicionRobot[0]+1][posicionRobot[1]] != "#"):
            print("Se puede mover una posición arriba")
            print("Posición con cordenadas: ", posicionRobot[0]+1, posicionRobot[1])
            distanciaDerecha = distanciaManhattan([ posicionRobot[0]+1, posicionRobot[1]], posicion_M[m])
            if(minimo> distanciaDerecha):
                minimo = distanciaDerecha
                siguientePosicion = [ posicionRobot[0]+1, posicionRobot[1]]
            print(distanciaDerecha)
        if(posicionRobot[0]-1 < tamanioMatriz and posicionRobot[0]-1 >= 0 and almacenActual[posicionRobot[0]-1][posicionRobot[1]] != "#"):
            print("Se puede mover una posición abajo")
            print("Posición con cordenadas: ", posicionRobot[0]-1, posicionRobot[1])    
            distanciaIzquierda = distanciaManhattan([ posicionRobot[0]-1, posicionRobot[1]], posicion_M[m])
            print(distanciaIzquierda)
            if(minimo>distanciaIzquierda):
                minimo= distanciaIzquierda
                siguientePosicion = [ posicionRobot[0]-1, posicionRobot[1]]


        almacenActual[posicionRobot[0]][posicionRobot[1]] = "0"
        almacenActual[siguientePosicion[0]][siguientePosicion[1]] = "R"
        print("Siguiente posicion = ", siguientePosicion)
        print(almacenActual[0])
        print(almacenActual[1])
        print(almacenActual[2])
        print(almacenActual[3])
        posicionRobot = siguientePosicion

    posicionRobot = siguientePosicion
    print("FIN PRIMER PARTE")
    posicionAnterior = siguientePosicion
    siguientePosicion = [-1,-1]
    minimo = 10000
    
    while siguientePosicion != posicion_M_Objetivo[m]:
        encontroSiguiente = False
        print(minimo)
        print("______________________")
        print("______________________")
        print("______________________")
        print("______________________")

        print("POSICIONES PRIMERO ANTERIOR DESPUES LA SIGUIENTE ",posicionAnterior, siguientePosicion)
        if(posicionRobot[1]-1 >= 0 and posicionRobot[1]-1 < tamanioMatriz):
            if( almacenActual[posicionRobot[0]][posicionRobot[1]-1] == "0"):
                print("Se puede mover una posición izquierda")
                print("Posición con cordenadas: ", posicionRobot[0], posicionRobot[1]-1)  
                distanciaArriba = distanciaManhattan([ posicionRobot[0], posicionRobot[1]-1], posicion_M_Objetivo[m])
                print(distanciaArriba)
                encontroSiguiente = True
                minimo = distanciaArriba
                siguientePosicion = [ posicionRobot[0], posicionRobot[1]-1]
                if(siguientePosicion == posicionAnterior):
                        minimo = 10000
                        encontroSiguiente = False
        
        if(posicionRobot[1]+1 >= 0 and posicionRobot[1]+1 < tamanioMatriz):
            if(almacenActual[posicionRobot[0]][posicionRobot[1]+1] == "0"):
                print("Se puede mover una posición derecha")
                print("Posición con cordenadas: ", posicionRobot[0], posicionRobot[1]+1)  
                distanciaAbajo = distanciaManhattan([ posicionRobot[0], posicionRobot[1]+1], posicion_M_Objetivo[m])
                print(distanciaAbajo)
                if(minimo>distanciaAbajo):
                    encontroSiguiente = True
                    minimo = distanciaAbajo
                    siguientePosicion = [ posicionRobot[0], posicionRobot[1]+1]
                    if(siguientePosicion == posicionAnterior):
                        minimo = 10000
                        encontroSiguiente = False

        if(posicionRobot[0]+1 >= 0 and posicionRobot[0]+1 < tamanioMatriz ):
            if(almacenActual[posicionRobot[0]+1][posicionRobot[1]] == "0"):
                print("Se puede mover una posición abajo")
                print("Posición con cordenadas: ", posicionRobot[0]+1, posicionRobot[1])
                distanciaDerecha = distanciaManhattan([ posicionRobot[0]+1, posicionRobot[1]], posicion_M_Objetivo[m])
                if(minimo>distanciaDerecha):
                    minimo = distanciaDerecha
                    siguientePosicion = [ posicionRobot[0]+1, posicionRobot[1]]
                    if(siguientePosicion == posicionAnterior):
                        print("Son iguales")
                        minimo = 10000
                        encontroSiguiente = False
                    print("POSICIONES PRIMERO ANTERIOR DESPUES LA SIGUIENTE ",posicionAnterior, siguientePosicion)
                    print("SIGUIENTE POSICION +++" , [ posicionRobot[0]+1, posicionRobot[1]])

                encontroSiguiente = True
                print(distanciaDerecha)
        if(posicionRobot[0]-1 < tamanioMatriz and posicionRobot[0]-1 >= 0 ):
            if( almacenActual[posicionRobot[0]-1][posicionRobot[1]] == "0"):
                print("Se puede mover una posición arriba")
                print("Posición con cordenadas: ", posicionRobot[0]-1, posicionRobot[1])    
                distanciaIzquierda = distanciaManhattan([ posicionRobot[0]-1, posicionRobot[1]], posicion_M_Objetivo[m])
                print(distanciaIzquierda)
                if(minimo>distanciaIzquierda):
                    encontroSiguiente = True
                    minimo= distanciaIzquierda
                    siguientePosicion = [ posicionRobot[0]-1, posicionRobot[1]]
                    print("Siguiente posicion--------------", siguientePosicion)
                    if(siguientePosicion == posicionAnterior):
                        minimo = 10000
                        encontroSiguiente= False


      
                
        if(encontroSiguiente == False):
            auxMomentaneo = siguientePosicion
            siguientePosicion = posicionAnterior
            posicionAnterior = auxMomentaneo
            minimo = 1000
        

        print("POSICIONES PRIMERO ANTERIOR DESPUES LA SIGUIENTE ",posicionAnterior, siguientePosicion)

        print("Siguiente posicion = ", siguientePosicion)
        almacenActual[posicionRobot[0]][posicionRobot[1]] = "0"
        almacenActual[siguientePosicion[0]][siguientePosicion[1]] = str(m+1)
        print("Siguiente posicion = ", siguientePosicion)
        print(almacenActual[0])
        print(almacenActual[1])
        print(almacenActual[2])
        print(almacenActual[3])
        posicionRobot = siguientePosicion
        
    if( almacenActual[posicion_M[m][0]][posicion_M[m][1]] == "R"):
        almacenActual[posicion_M[m][0]][posicion_M[m][1]] = "0"
    almacenActual[posicion_M_Objetivo[m][0]] [posicion_M_Objetivo[m][1]] = str(m+1) 
    posicion_M[m] = siguientePosicion
    return almacenActual




for x in range(3):
    costeInicio = [0,0,0]
    puntoMasCercano = 0

    for x in range(numInventarios):
        print("**********************************************")
        print("El coste para el punto numero, M", x+1 , " es: ")
        if posicion_M[x] != posicion_M_Objetivo[x]:
            costeInicio[x] = distanciaManhattan(posicion_R,posicion_M[x])
        else:
            costeInicio[x] = 10000
        print(costeInicio[x])
    
    puntoMasCercano = costeInicio.index(min(costeInicio))
    print("Punto más cercano ", puntoMasCercano)
    almacen = acomodarAlmacen(almacen,posicion_R,4,puntoMasCercano)


print(posicion_M)
print(posicion_M_Objetivo)
print(almacen)
print(posicion_R)





"""


print("punto mas cercano", puntoMasCercano)
for i, fila in enumerate(almacen):
    for j, valor in enumerate(fila):
        if valor == str(puntoMasCercano+1):
            posicion_R[0] = j
            posicion_R[1] = i
            break
print("Posicion inicial de robot ", posicion_R)
print(posicion_R)
for x in range(numInventarios):
        print("**********************************************")
        print("El coste para el punto numero, M", x+1 , " es: ")
        if posicion_M[x] != posicion_M_Objetivo[x]:
            costeInicio[x] = distanciaManhattan(posicion_R,posicion_M[x])
        else:
            costeInicio[x] = 10000
        print(costeInicio[x])
almacen = acomodarAlmacen(almacen,posicion_R,4,2)

"""





"""
    Pendientes sumar g en la distancia de manhattan por cada paso 
    Ejecutar por cada punto a ordenar 
    Ordenar puntos a ordenar en el orden en que se hará la ejecución considerando la distancia de manhattan 

"""

