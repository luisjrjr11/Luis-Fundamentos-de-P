def buscar_valor(matriz, valor_a_buscar):
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == valor_a_buscar:
                return True, i, j

    return False, None, None

# Definir una matriz de ejemplo de 3x3
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar en la matriz
valor_a_buscar = 5

# Realizar la búsqueda
encontrado, fila, columna = buscar_valor(matriz_ejemplo, valor_a_buscar)

# Mostrar el resultado
if encontrado:
    print(f"¡El valor {valor_a_buscar} se encontró en la posición ({fila + 1}, {columna + 1}) de la matriz!")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
