import random

# Definir ciudades, días de la semana y semanas
ciudades = ['Ciudad A', 'Ciudad B', 'Ciudad C']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4

# Crear una matriz 3D con valores aleatorios de temperatura
temperaturas = [[[random.randint(20, 35) for _ in range(semanas)] for _ in range(len(dias_semana))] for _ in range(len(ciudades))]

# Mostrar la matriz de temperaturas
print("Matriz de Temperaturas:")
for i, ciudad in enumerate(ciudades):
    for j, dia in enumerate(dias_semana):
        print(f"{ciudad}, {dia}: {temperaturas[i][j]}")

# Calcular el promedio de temperaturas por ciudad y semana
for i, ciudad in enumerate(ciudades):
    for j, dia in enumerate(dias_semana):
        promedio_semana = sum(temperaturas[i][j]) / semanas
        print(f"Promedio de temperatura en {ciudad}, {dia}: {promedio_semana:.2f}°C")

    promedio_ciudad = sum(temperaturas[i][j][k] for j in range(len(dias_semana)) for k in range(semanas)) / (len(dias_semana) * semanas)
    print(f"Promedio de temperatura en {ciudad} durante la semana: {promedio_ciudad:.2f}°C")
    print("\n")
