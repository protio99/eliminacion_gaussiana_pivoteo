matriz_aumentada = [[5, 6, 1, 4], [8, 5, 4, 5], [7, 1, 7, 6], [5, 4, 4, 7]]
terminos_independientes = [4, 5, 6, 7]

#Imprime la lista en el formato de una matriz, para una mejor visualizacion
def imprime_matriz(matriz):
    for i in matriz:
        for j in i:
            print(j, end="  ")
        print("")

print("Matriz aumentada sin ordenar")
imprime_matriz(matriz_aumentada)

#Calcula el valor maximo de cada fila y lo almacena en una lista
def calc_factores_escala(matriz):
    factores_escala = []
    for i in matriz:
        #Convertimos todos los valores de la fila en valores absolutos
        valores_absolutos = [abs(n) for n in i]
        #Ordenamos la fila de mayor a menor para obtener el factor de escala, es decir, el mayor valor de cada fila
        factor_escala = sorted(valores_absolutos, reverse=True)[0]
        #Almacenamos el factor de escala en una lista y la retornamos para su uso posterior
        factores_escala.append(factor_escala)
    print(factores_escala)
    return factores_escala

#Calculo de los cocientes rk para la primera columna
def calc_cocientes(matriz, factores_escala):
    print("Matriz aumentada desde el metodo de cocientes")
    imprime_matriz(matriz)
    cocientes = []
    max_cociente = 0
    max_factor_escala = 0
    fila_max_factor_escala = 0
    #Llamamos a todos los terminos de la primera columna y los dividimos por los factores de escala
    for i in range(len(matriz)):
        #Para obtener los cocientes, debemos redondear el valor absoluto de la division de los terminos de la primera columna entre los factores de escala
        cociente = round(abs(matriz[i][0]) / factores_escala[i],3)
        cocientes.append(cociente)
        #Obtenemos el maximo cociente y el factor de escala correspondiente en cada iteracion
        if cociente >= max_cociente and factores_escala[i] > max_factor_escala:
            max_cociente = cociente
            max_factor_escala = factores_escala[i]
            fila_max_factor_escala = i
    print("Cocientes", cocientes)
    print("Maximo cociente", max_cociente)
    print("Maximo factor de escala", max_factor_escala)
    print("Fila con maximo factor de escala", fila_max_factor_escala)
    return cocientes, max_cociente, max_factor_escala, fila_max_factor_escala
    
print("Factores escala")
factores_escala = calc_factores_escala(matriz_aumentada)
print("Tamaño de la matriz", len(matriz_aumentada))
calc_cocientes(matriz_aumentada, factores_escala)