# Sistema Inteligente de Rutas - Actividad 2 de Inteligencia Artificial

# Lugares disponibles (número de opción: nombre del lugar)
lugares = {
    "1": "Mi casa",
    "2": "Minimarket del barrio",
    "3": "Biblioteca",
    "4": "Estadio de fútbol",
    "5": "Universidad",
    "6": "Oficina de trabajo",
    "7": "Restaurante",
}

# Base de conocimiento: conexiones entre los lugares
conexiones = {
    "Mi casa": ["Minimarket del barrio", "Biblioteca"],
    "Minimarket del barrio": ["Mi casa", "Biblioteca", "Estadio de fútbol"],
    "Biblioteca": ["Mi casa", "Minimarket del barrio", "Universidad"],
    "Estadio de fútbol": ["Minimarket del barrio", "Restaurante"],
    "Universidad": ["Biblioteca", "Oficina de trabajo"],
    "Oficina de trabajo": ["Universidad", "Restaurante"],
    "Restaurante": ["Estadio de fútbol", "Oficina de trabajo"],
}

# Reglas de dirección: (desde, hasta) -> indicación
indicaciones = {
    ("Mi casa", "Minimarket del barrio"): "Sal de Mi casa, gira a la derecha y avanza una cuadra por la Calle 1.",
    ("Minimarket del barrio", "Mi casa"): "Sal del Minimarket, gira a la izquierda y regresa una cuadra por la Calle 1.",
    ("Mi casa", "Biblioteca"): "Sal de Mi casa, gira a la izquierda y avanza dos cuadras por la Carrera 2.",
    ("Biblioteca", "Mi casa"): "Sal de la Biblioteca y avanza dos cuadras por la Carrera 2.",
    ("Minimarket del barrio", "Biblioteca"): "Sigue derecho dos cuadras y gira a la izquierda.",
    ("Biblioteca", "Minimarket del barrio"): "Gira a la derecha y avanza dos cuadras.",
    ("Minimarket del barrio", "Estadio de fútbol"): "Toma la Calle del Parque y avanza tres cuadras hasta el Estadio.",
    ("Estadio de fútbol", "Minimarket del barrio"): "Toma la Calle del Parque y avanza tres cuadras hasta el Minimarket.",
    ("Biblioteca", "Universidad"): "Continúa por la Avenida Central tres cuadras hasta la Universidad.",
    ("Universidad", "Biblioteca"): "Toma la Avenida Central y avanza tres cuadras hasta la Biblioteca.",
    ("Universidad", "Oficina de trabajo"): "Sal de la Universidad, gira a la derecha y avanza dos cuadras.",
    ("Oficina de trabajo", "Universidad"): "Sal de la Oficina, gira a la izquierda y avanza dos cuadras.",
    ("Oficina de trabajo", "Restaurante"): "Continúa una cuadra por la Calle 8 y gira a la izquierda.",
    ("Restaurante", "Oficina de trabajo"): "Sal del Restaurante, gira a la derecha y avanza una cuadra por la Calle 8.",
    ("Estadio de fútbol", "Restaurante"): "Rodea el Estadio por el costado oriental y avanza dos cuadras.",
    ("Restaurante", "Estadio de fútbol"): "Desde el Restaurante avanza dos cuadras hacia el Estadio.",
}

# Mostrar los lugares disponibles
def mostrar_lugares():
    print("\nLugares disponibles:\n")
    for numero in lugares:
        print(f"{numero}. {lugares[numero]}")
    print()

# Pedir un lugar y validar que la opción exista
def pedir_lugar(mensaje):
    opcion = input(mensaje).strip()
    while opcion not in lugares:
        print("La opción ingresada no existe.")
        opcion = input(mensaje).strip()
    return lugares[opcion]

# Buscar la mejor ruta con búsqueda en anchura (BFS)
def buscar_ruta(origen, destino):
    rutas_pendientes = [[origen]]  # Rutas por revisar
    visitados = [origen]           # Lugares ya visitados

    while len(rutas_pendientes) > 0:
        ruta = rutas_pendientes.pop(0)  # Tomar la primera ruta
        lugar_actual = ruta[-1]         # Revisar el último lugar

        # Si es el destino, retornar la ruta
        if lugar_actual == destino:
            return ruta

        # Revisar lugares conectados
        for vecino in conexiones[lugar_actual]:
            if vecino not in visitados:
                visitados.append(vecino)
                rutas_pendientes.append(ruta + [vecino])  # Nueva posible ruta

    # No existe una ruta
    return []

# Mostrar la ruta encontrada y sus indicaciones
def mostrar_ruta(ruta):
    print("\nRuta encontrada:\n")
    print(" -> ".join(ruta))

    # Mostrar indicaciones
    print("\nIndicaciones:\n")
    for i in range(len(ruta) - 1):
        paso = (ruta[i], ruta[i + 1])  # Tupla (desde, hasta)
        print(f"{i + 1}. {indicaciones[paso]}\n")

    print(f"Número de lugares: {len(ruta)}")

# Programa principal
print("=" * 40)
print("       SISTEMA INTELIGENTE DE RUTAS")
print("=" * 40)

respuesta = "S"
while respuesta == "S":
    mostrar_lugares()
    origen = pedir_lugar("Seleccione el origen: ")
    destino = pedir_lugar("Seleccione el destino: ")

    # Buscar la mejor ruta
    ruta = buscar_ruta(origen, destino)

    # Validar y mostrar el resultado
    if origen == destino:
        print(f"\nYa te encuentras en {origen}.")
    elif len(ruta) == 0:
        print("\nNo existe una ruta disponible.")
    else:
        mostrar_ruta(ruta)

    # Preguntar si desea buscar otra ruta
    respuesta = input("\n¿Desea buscar otra ruta? S/N ").strip().upper()

print("\nGracias por usar el sistema.")
