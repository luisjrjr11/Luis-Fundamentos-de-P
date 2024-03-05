def temperatura_promedio(datos):
    promedios_por_ciudad = {}

    for ciudad_data in datos:
        ciudad = ciudad_data['ciudad']
        temperaturas = ciudad_data['temperaturas']
        promedio = sum(temperaturas) / len(temperaturas)
        promedios_por_ciudad[ciudad] = promedio

    return promedios_por_ciudad

# Ejemplo de uso con datos de 3 ciudades durante 4 semanas
datos_ejemplo = [
    {'ciudad': 'CiudadA', 'temperaturas': [25, 28, 23, 26]},
    {'ciudad': 'CiudadB', 'temperaturas': [22, 24, 20, 21]},
    {'ciudad': 'CiudadC', 'temperaturas': [30, 32, 28, 29]}
]

resultados = temperatura_promedio(datos_ejemplo)

# Imprimir los resultados
for ciudad, promedio in resultados.items():
    print(f"La temperatura promedio en {ciudad} es: {promedio}°C")