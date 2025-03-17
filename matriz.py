import numpy as np

matriz = [[4, 3, 1], [4, 11, -1], [6, 2, 4]]
terminos_independientes = [4, 5, 6, 7]

#Imprime la lista en el formato de una matriz, para una mejor visualizacion
def imprime_matriz(matriz):
    for fila in matriz:
        print("  ".join(f"{num:8.2f}" for num in fila))
    print("")

#Calculo de los factores escala para cada fila
def calc_factores_escala(A):
    #Obtiene el mayor valor absoluto de cada fila, donde A es la matriz aumentada
    factores_escala = np.max(np.abs(A), axis=1)
    print("Factores escala: ", factores_escala)
    return factores_escala

# Calculo de los cocientes rk para cada columna para el pivotaje
def calc_cocientes(A, factores_escala, k):
    #A: matriz
    #k: Columna en iteración
    cocientes = np.abs(A[k:, k]) / factores_escala[k:]  # Cálculo vectorizado
    max_index = k + np.argmax(cocientes)  # Encuentra el índice de la mejor fila pivote
    return max_index

def calc_cocientes(matriz, factores_escala, iteracion):
    print("Matriz aumentada desde el metodo de cocientes")
    imprime_matriz(matriz)
    cocientes = []
    max_cociente = 0
    max_factor_escala = 0
    fila_max_factor_escala = 0
    index = 0
    for i in range(iteracion, len(matriz)):
        print("Valor de i: ", i)
        cociente = round(abs(matriz[i][iteracion]) / factores_escala[index], 3)
        print("Divisor: ", abs(matriz[i][iteracion]), "Dividendo: ", factores_escala[index] )
        cocientes.append(cociente)
        print("Index ", index, " en iteracion ", i)
        print("Cociente: ", cociente, "Max cociente: ", max_cociente, "Factor escala: ", factores_escala[index])
        if cociente >= max_cociente and factores_escala[index] > max_factor_escala:
            print("Entre al if (cociente, factor escala): ", cociente, factores_escala[index])
            max_cociente = cociente
            max_factor_escala = factores_escala[index]
            fila_max_factor_escala = index
        index += 1
        
        print("=============================")

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
    print("Matriz que entra al metodo de eliminacion: ")
    imprime_matriz(matriz_actual)
    fila_pivote = matriz_actual[iteracion]
    print("Fila pivote:", fila_pivote)
    for i in range(iteracion, len(matriz_actual)):
        fila = matriz_actual[i + 1]
        print("Fila: ", fila, " en iteracion i: ", i)
        for j in range(0, len(fila)):
            multiplicador = (fila[j]/pivote) * fila_pivote[j]
            nuevo_valor = matriz_actual[fila][j] - multiplicador
            matriz_actual[fila][j] = nuevo_valor
            print("multiplicador: ", multiplicador)
            print("matriz tras eliminacion en paso: " , j)
            imprime_matriz(matriz_actual)

            
        # print("Fila | Multiplicador : ", fila, multiplicador)





# for iteracion in range (0, 1):
#     nueva_matriz = []
#     if len(nueva_matriz) > 0: 
#         matriz = nueva_matriz

#     factores = calc_factores_escala(matriz, iteracion)
#     cocientes, max_cociente, max_factor_escala, fila_max_factor_escala = calc_cocientes(matriz, factores, iteracion)    
#     nueva_matriz = intercambio_fila(matriz, iteracion, fila_max_factor_escala)
#     nueva_matriz = eliminacion(nueva_matriz, iteracion, max_factor_escala )

A = np.array([[2, 3, 1, 4], [4, 1, 3 , 2], [3, 4, 2, 1], [5, 2, 4, 3]], dtype=float)
b = np.array([10, 5, 7, 8], dtype=float)

print("-----------------------CALCULO DE LOS FACTORES ESCALA-----------------------------")
factores = calc_factores_escala(A)
print("")
# print("-----------------------CALCULO DE LOS COCIENTES ----------------------------------")
# cocientes, max_cociente, max_factor_escala, fila_max_factor_escala = calc_cocientes(matriz, factores, 0)    
# print("")
# print("---------------------------INTERCAMBIO DE FILAS ----------------------------------")
# nueva_matriz = intercambio_fila(matriz, 0, fila_max_factor_escala)
# print("")
# print("-------------------------------ELIMINACION ---------------------------------------")
# nueva_matriz = eliminacion(nueva_matriz, 0, max_factor_escala )



