from heapq import heappop, heappush
import copy 

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
posicion_R = (-1,-1)
for i, fila in enumerate(almacen):
    for j, valor in enumerate(fila):
        if valor == 'R':
            posicion_R = (j,i)
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
print("Posicion de inventarios Estado inicial")        
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
print("Posicion de inventarios Objetivos ")        
for x in range(numInventarios):
    print("M",x+1,":",posicion_M_Objetivo[x])




def distanciaManhattan(x,y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


DIRECCIONES = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def imprimirCamino(aux, camino):
    gridImp = copy.deepcopy(aux)
    count_1 = 0
    for x in camino:
        print("___")
        gridImp[x[0]][x[1]] = 'R'
        print(gridImp[0])
        print(gridImp[1])
        print(gridImp[2])
        print(gridImp[3])
        gridImp[x[0]][x[1]] = '0'
        count_1 += 1



def a_estrella(inicio, objetivo, grid,m, eliminar):
    """Implementa el algoritmo A* para encontrar el camino más corto en un grid."""
    filas, columnas = len(grid), len(grid[0])
    open_set = []
    heappush(open_set, (0, inicio))
    came_from = {}
    g_cost = {inicio: 0}
    f_cost = {inicio: distanciaManhattan(inicio, objetivo)}
    print(filas, columnas)

    while open_set:
        _, actual = heappop(open_set)

        if actual == objetivo:
            # Reconstruir el camino
            camino = []
            while actual in came_from:
                camino.append(actual)
                actual = came_from[actual]
            camino.append(inicio)
            camino.reverse()
            imprimirCamino(grid, camino)
            if(eliminar % 2 != 0 or eliminar <= 1):
                print("Cambia el valor de la casilla a 0 ")
                grid[inicio[0]][inicio[1]] = '0'
                grid[objetivo[0]][objetivo[1]] = str(m+1)
            else:
                grid[objetivo[0]][objetivo[1]] = str(m+1)
            posicion_M[m] = posicion_M_Objetivo[m]
            return camino, grid

        for d in DIRECCIONES:
            vecino = (actual[0] + d[0], actual[1] + d[1])
            if 0 <= vecino[0] < filas and 0 <= vecino[1] < columnas and grid[vecino[0]][vecino[1]] != '#':
                tentative_g_cost = g_cost[actual] + 1
                if vecino not in g_cost or tentative_g_cost < g_cost[vecino]:
                    came_from[vecino] = actual
                    g_cost[vecino] = tentative_g_cost
                    f_cost[vecino] = tentative_g_cost + distanciaManhattan(vecino, objetivo)
                    heappush(open_set, (f_cost[vecino], vecino))

    return []  # Retorna una lista vacía si no se encuentra un camino

# Ejemplo de uso

count = 0
for y in range(3):
    costeInicio = [0,0,0]
    puntoMasCercano = 0
    for x in range(numInventarios):
        print("******")
        print("El coste para el punto numero, M", x+1 , " es: ")
        if posicion_M[x] != posicion_M_Objetivo[x]:
            costeInicio[x] = distanciaManhattan(posicion_R,posicion_M[x])
        else:
            costeInicio[x] = 10000
        print(costeInicio[x])
    puntoMasCercano = costeInicio.index(min(costeInicio))
    print("Punto más cercano ", puntoMasCercano)    
    objetivo = (posicion_M[puntoMasCercano][0], posicion_M[puntoMasCercano][1])
    print(posicion_R, objetivo)
    camino, almacen = a_estrella(posicion_R, objetivo, almacen,puntoMasCercano, count)
    print("RETORNO DE FUNCION *******")
    print(almacen[0])
    print(almacen[1])
    print(almacen[2])
    print(almacen[3])
    count += 1
    print("Camino encontrado:", camino)
    posicion_R = objetivo
    objetivo = (posicion_M_Objetivo[puntoMasCercano][0], posicion_M_Objetivo[puntoMasCercano][1])
    camino, almacen = a_estrella(posicion_R, objetivo, almacen,puntoMasCercano, count)
    print("Camino encontrado:", camino)
    posicion_R = objetivo
    count += 1
    print("RETORNO DE FUNCION *******")
    print(almacen[0])
    print(almacen[1])
    print(almacen[2])
    print(almacen[3])


    """
        LZSG
    """