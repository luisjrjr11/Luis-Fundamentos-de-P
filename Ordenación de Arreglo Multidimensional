def ordenar_fila(matriz, numero_fila):
    fila_a_ordenar = matriz[numero_fila]
    n = len(fila_a_ordenar)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if fila_a_ordenar[j] > fila_a_ordenar[j + 1]:
                fila_a_ordenar[j], fila_a_ordenar[j + 1] = fila_a_ordenar[j + 1], fila_a_ordenar[j]

# Definir una matriz de ejemplo de 3x3
matriz_ejemplo = [
    [9, 3, 7],
    [5, 1, 6],
    [2, 8, 4]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz_ejemplo:
    print(fila)

# Elegir una fila para ordenar (puedes cambiar el número según tu preferencia)
numero_fila_a_ordenar = 1

# Llamar a la función para ordenar la fila seleccionada
ordenar_fila(matriz_ejemplo, numero_fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz_ejemplo:
    print(fila)
