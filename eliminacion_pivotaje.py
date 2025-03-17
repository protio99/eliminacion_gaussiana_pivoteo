import numpy as np

# ------------------- FUNCIONES -------------------

#Imprime la lista en el formato de una matriz, redondeando cada elemento de la matriz a dos cifras
def imprime_matriz(A, b):
    #A: matriz
    #b: Vector de terminos independientes
    matriz_aumentada = np.hstack((A, b.reshape(-1, 1)))
    for fila in matriz_aumentada:
        print("  ".join(f"{num:8.2f}" for num in fila[:-1]) + "  |" + f" {fila[-1]:8.2f}")
    print("")

#Calculo del determinante de la matriz para validar si esta tiene o no solucion
def calcular_determinante(A):
    return np.linalg.det(A)

# Calculo de los factores escala para cada fila, obteniendo el mayor valor absoluto de cada fila
def calc_factores_escala(A):
    return np.max(np.abs(A), axis=1)

# Calculo de los cocientes rk para cada columna para el pivotaje
def calc_cocientes(A, factores_escala, k):
    #A: matriz
    #k: Columna en iteración
    cocientes = np.abs(A[k:, k]) / factores_escala[k:]  # Cálculo vectorizado
    max_index = k + np.argmax(cocientes)  # Encuentra el índice de la mejor fila pivote
    return max_index

# Se encarga de intercambiar las filas segun la que tenga el mejor pivote
def intercambio_fila(A, b, k, fila_pivote):
    #A: matriz
    #b: Vector de terminos independientes
    #k: Indice de la fila actual que se debe intercambiar
    #fila_pivote: Indice de la fila con el mejor pivote 
    if k != fila_pivote:
        A[[k, fila_pivote]] = A[[fila_pivote, k]]
        b[[k, fila_pivote]] = b[[fila_pivote, k]]

#Realiza la eliminacion gaussiana teniendo en cuenta el pivotaje parcial escalado 
def eliminacion_gauss(A, b):
    #A: matriz
    #b: Vector de terminos independientes
    n = len(A)
    #n: tamaño de la matriz
    factores_escala = calc_factores_escala(A)

    print("\nInicio del proceso de eliminación:")
    for k in range(n):
        #k: Columna actual de eliminacion
        print(f"======================Iteración: {k+1} ======================")
        print(f"Factores escala: {factores_escala}")
        
        # Pivotaje parcial escalado
        fila_pivote = calc_cocientes(A, factores_escala, k)
        print(f"Fila pivote: {fila_pivote}")

        intercambio_fila(A, b, k, fila_pivote)
        print("Matriz después del intercambio de filas:")
        imprime_matriz(A, b)

        # Eliminación de las filas inferiores
        for i in range(k + 1, n):
            #i: Cada fila debajo de k
            factor = A[i, k] / A[k, k]
            # Restamos la fila pivote escalada
            A[i, k:] -= factor * A[k, k:] 
            # Restamos en el vector de términos independientes 
            b[i] -= factor * b[k] 
        
        print("Matriz después de la eliminación de filas:")
        imprime_matriz(A, b)
        print("=========================================================")

    return A, b

#Metodo para resolver el sistema por medio de sustitucion regresiva despues de tener la matriz triangular superior
def sustitucion_regresiva(A, b):
    #A: matriz
    #b: Vector de terminos independientes
    #n: tamaño de la matriz
    n = len(A)
    #x: Vector de soluciones inicializado en cero
    x = np.zeros(n)

    #La iteracion se realiza de abajo hacia arriba, se multiplican lo coeficientes por los valores ya calculados
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return np.round(x, 2)



# ------------------- PROGRAMA PRINCIPAL -------------------

# Matriz de coeficientes (A) y vector de términos independientes (b)
A = np.array([[4, 3, 1, 2],
              [2, 6, 4, 8],
              [1, 1, 3, 1],
              [2, 4, 2, 6]], dtype=float)
b = np.array([5, 7, 3, 8], dtype=float)

print("Matriz aumentada inicial (A | b):")
imprime_matriz(A, b)

# Cálculo del determinante antes de la eliminación
det_A = calcular_determinante(A)
print(f"Determinante de la matriz: {det_A:.1f}")

if np.abs(det_A) < 1e-10:
    print("El sistema NO TIENE solución única porque su determinante es 0 o muy cercano a 0.")
else:
    print("El sistema TIENE solución única porque su determinante es diferente de cero. Iniciando proceso...")

    # Aplicamos el método de eliminación gaussiana con pivotaje parcial escalado
    A_triangular, b_modificado = eliminacion_gauss(A, b)

    print("Matriz triangular superior:")
    imprime_matriz(A_triangular, b_modificado)

    # Resolvemos el sistema con sustitución regresiva
    solucion = sustitucion_regresiva(A_triangular, b_modificado)
    print("Solución del sistema:", solucion)
