matriz = [[5, 6, 1, 4], [8, 5, 4, 5], [7, 1, 7, 6], [5, 4, 4, 7]]
terminos_independientes = [4, 5, 6, 7]

#Imprime la lista en el formato de una matriz, para una mejor visualizacion
def imprime_matriz(matriz):
    for i in matriz:
        for j in i:
            print(j, end="  ")
        print("")

print("Matriz aumentada sin ordenar")
imprime_matriz(matriz)

def calc_factores_escala(matriz, iteracion):
    factores_escala = []
    for i in range(iteracion, len(matriz)):
        fila = matriz[i]
        valores_absolutos = [abs(j) for j in fila]
        factor_escala = sorted(valores_absolutos, reverse=True)[0]
        factores_escala.append(factor_escala)
    print(factores_escala)
    return factores_escala

# Calculo de los cocientes rk para cada columna
def calc_cocientes(matriz, factores_escala, iteracion):
    print("Matriz aumentada desde el metodo de cocientes")
    imprime_matriz(matriz)
    cocientes = []
    max_cociente = 0
    max_factor_escala = 0
    fila_max_factor_escala = 0
    index = 0
    for i in range(iteracion, len(matriz)):
        cociente = round(abs(matriz[i][iteracion]) / factores_escala[index],3)
        cocientes.append(cociente)
        print("")
        if cociente >= max_cociente and factores_escala[index] > max_factor_escala:
            print("Entre al if (cociente, factor escala): ", cociente, factores_escala[index])
            max_cociente = cociente
            max_factor_escala = factores_escala[index]
            fila_max_factor_escala = index
            index += 1

    print("Cocientes", cocientes)
    print("Maximo cociente", max_cociente)
    print("Maximo factor de escala", max_factor_escala)
    print("Fila con maximo factor de escala", fila_max_factor_escala)
    return cocientes, max_cociente, max_factor_escala, fila_max_factor_escala

def intercambio_fila(matriz_actual, iteracion, fila_max_factor_escala):

    print("Matriz en el intercambio de filas: ")
    imprime_matriz(matriz_actual)

    fila_actual = matriz_actual[iteracion]
    fila_mejor_pivote = matriz_actual[fila_max_factor_escala]
    print("Fila actual | Fila mejor pivote: ", fila_actual, fila_mejor_pivote)

    #Intercambio de filas
    matriz_actual[iteracion] = fila_mejor_pivote
    matriz_actual[fila_max_factor_escala] = fila_actual

    print("Matriz intercambiada: ")
    imprime_matriz(matriz_actual)
    return matriz_actual

def eliminacion(matriz_actual, iteracion, pivote):
    print("Entramos en el metodo de eliminacion")
    fila_pivote = matriz_actual[iteracion]
    print("Pivote en iteracion:", pivote)
    for i in range(iteracion, len(matriz_actual)):
        fila = matriz_actual[i + 1]
        print("Fila: ", fila)
        for j in range(0, len(fila)):
            multiplicador = (fila[j]/pivote) * fila_pivote[j]
            nuevo_valor = matriz_actual[fila][j] - multiplicador
            matriz_actual[fila][j] = nuevo_valor
            print("multiplicador: ", multiplicador)
            print("matriz tras eliminacion en paso: " , j)
            imprime_matriz(matriz_actual)

            
        # print("Fila | Multiplicador : ", fila, multiplicador)





for iteracion in range (0, len(matriz) - 1):
    nueva_matriz = []
    if len(nueva_matriz) > 0: 
        matriz = nueva_matriz

    factores = calc_factores_escala(matriz, iteracion)
    cocientes, max_cociente, max_factor_escala, fila_max_factor_escala = calc_cocientes(matriz, factores, iteracion)    
    nueva_matriz = intercambio_fila(matriz, iteracion, fila_max_factor_escala)
    nueva_matriz = eliminacion(nueva_matriz, iteracion, max_factor_escala )
