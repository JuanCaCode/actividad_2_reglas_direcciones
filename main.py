# Sistema Inteligente de Rutas - Actividad 2 de Inteligencia Artificial

# Nombres de los lugares (se definen una sola vez)
CASA = "Mi casa"
MINIMARKET = "Minimarket del barrio"
BIBLIOTECA = "Biblioteca"
ESTADIO = "Estadio de fútbol"
UNIVERSIDAD = "Universidad"
OFICINA = "Oficina de trabajo"
RESTAURANTE = "Restaurante"

# Lugares disponibles (número de opción: lugar)
lugares = {
    "1": CASA,
    "2": MINIMARKET,
    "3": BIBLIOTECA,
    "4": ESTADIO,
    "5": UNIVERSIDAD,
    "6": OFICINA,
    "7": RESTAURANTE,
}

# Base de conocimiento: conexiones entre los lugares
conexiones = {
    CASA: [MINIMARKET, BIBLIOTECA],
    MINIMARKET: [CASA, BIBLIOTECA, ESTADIO],
    BIBLIOTECA: [CASA, MINIMARKET, UNIVERSIDAD],
    ESTADIO: [MINIMARKET, RESTAURANTE],
    UNIVERSIDAD: [BIBLIOTECA, OFICINA],
    OFICINA: [UNIVERSIDAD, RESTAURANTE],
    RESTAURANTE: [ESTADIO, OFICINA],
}

# Reglas de dirección: (desde, hasta) -> indicación
indicaciones = {
    (CASA, MINIMARKET): "Sal de Mi casa, gira a la derecha y avanza una cuadra por la Calle 1.",
    (MINIMARKET, CASA): "Sal del Minimarket, gira a la izquierda y regresa una cuadra por la Calle 1.",
    (CASA, BIBLIOTECA): "Sal de Mi casa, gira a la izquierda y avanza dos cuadras por la Carrera 2.",
    (BIBLIOTECA, CASA): "Sal de la Biblioteca y avanza dos cuadras por la Carrera 2.",
    (MINIMARKET, BIBLIOTECA): "Sigue derecho dos cuadras y gira a la izquierda.",
    (BIBLIOTECA, MINIMARKET): "Gira a la derecha y avanza dos cuadras.",
    (MINIMARKET, ESTADIO): "Toma la Calle del Parque y avanza tres cuadras hasta el Estadio.",
    (ESTADIO, MINIMARKET): "Toma la Calle del Parque y avanza tres cuadras hasta el Minimarket.",
    (BIBLIOTECA, UNIVERSIDAD): "Continúa por la Avenida Central tres cuadras hasta la Universidad.",
    (UNIVERSIDAD, BIBLIOTECA): "Toma la Avenida Central y avanza tres cuadras hasta la Biblioteca.",
    (UNIVERSIDAD, OFICINA): "Sal de la Universidad, gira a la derecha y avanza dos cuadras.",
    (OFICINA, UNIVERSIDAD): "Sal de la Oficina, gira a la izquierda y avanza dos cuadras.",
    (OFICINA, RESTAURANTE): "Continúa una cuadra por la Calle 8 y gira a la izquierda.",
    (RESTAURANTE, OFICINA): "Sal del Restaurante, gira a la derecha y avanza una cuadra por la Calle 8.",
    (ESTADIO, RESTAURANTE): "Rodea el Estadio por el costado oriental y avanza dos cuadras.",
    (RESTAURANTE, ESTADIO): "Desde el Restaurante avanza dos cuadras hacia el Estadio.",
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
