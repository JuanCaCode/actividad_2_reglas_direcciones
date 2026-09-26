# Pruebas del Sistema Inteligente de Rutas

Pruebas realizadas el 26 de septiembre de 2026 con `python main.py` (Python 3.14.7, Windows 11). En cada prueba se muestra lo que aparece en la terminal después de la lista de lugares disponibles.

## Resumen

| Prueba | Caso | Resultado esperado | Estado |
| --- | --- | --- | --- |
| 1 | Mi casa -> Biblioteca | Ruta directa: Mi casa -> Biblioteca | Correcta |
| 2 | Mi casa -> Restaurante | Mi casa -> Minimarket del barrio -> Estadio de fútbol -> Restaurante | Correcta |
| 3 | Minimarket del barrio -> Universidad | Minimarket del barrio -> Biblioteca -> Universidad | Correcta |
| 4 | Universidad -> Universidad | Informa que ya se encuentra en el destino | Correcta |
| 5 | Opción inexistente | Mensaje de error y se vuelve a pedir la opción | Correcta |
| 6 | Buscar otra ruta (S/N) | Con S se hace otra búsqueda y con N termina el programa | Correcta |
| 7 | Ruta inexistente (prueba adicional) | Mensaje "No existe una ruta disponible." | Correcta |

## Prueba 1: Mi casa -> Biblioteca

**Entradas:** origen `1`, destino `3`.

**Resultado esperado:** ruta directa de 1 conexión, con una indicación y 2 lugares.

**Resultado obtenido:**

```text
Seleccione el origen: 1
Seleccione el destino: 3

Ruta encontrada:

Mi casa -> Biblioteca

Indicaciones:

1. Sal de Mi casa, gira a la izquierda y avanza dos cuadras por la Carrera 2.

Número de lugares: 2
```

**Estado:** Correcta.

## Prueba 2: Mi casa -> Restaurante

**Entradas:** origen `1`, destino `7`.

**Ruta esperada:** Mi casa -> Minimarket del barrio -> Estadio de fútbol -> Restaurante (3 conexiones). La otra ruta posible, por Biblioteca, Universidad y Oficina de trabajo, usa 4 conexiones.

**Resultado obtenido:**

```text
Seleccione el origen: 1
Seleccione el destino: 7

Ruta encontrada:

Mi casa -> Minimarket del barrio -> Estadio de fútbol -> Restaurante

Indicaciones:

1. Sal de Mi casa, gira a la derecha y avanza una cuadra por la Calle 1.

2. Toma la Calle del Parque y avanza tres cuadras hasta el Estadio.

3. Rodea el Estadio por el costado oriental y avanza dos cuadras.

Número de lugares: 4
```

**Estado:** Correcta.

## Prueba 3: Minimarket del barrio -> Universidad

**Entradas:** origen `2`, destino `5`.

**Ruta esperada:** Minimarket del barrio -> Biblioteca -> Universidad (2 conexiones). Pasar también por Mi casa usaría 3 conexiones.

**Resultado obtenido:**

```text
Seleccione el origen: 2
Seleccione el destino: 5

Ruta encontrada:

Minimarket del barrio -> Biblioteca -> Universidad

Indicaciones:

1. Sigue derecho dos cuadras y gira a la izquierda.

2. Continúa por la Avenida Central tres cuadras hasta la Universidad.

Número de lugares: 3
```

**Estado:** Correcta.

## Prueba 4: Universidad -> Universidad

**Entradas:** origen `5`, destino `5`.

**Resultado esperado:** el sistema informa que ya se encuentra en el destino y no muestra ninguna ruta.

**Resultado obtenido:**

```text
Seleccione el origen: 5
Seleccione el destino: 5

Ya te encuentras en Universidad.
```

**Estado:** Correcta.

## Prueba 5: Opción inexistente

**Entradas:** para el origen, `9` (número fuera del rango), `hola` (texto), Enter sin escribir nada y luego `1`. Para el destino, `0` y luego `6`.

**Resultado esperado:** con cada opción inexistente se muestra "La opción ingresada no existe." y se vuelve a pedir el dato, sin cerrar el programa.

**Resultado obtenido:**

```text
Seleccione el origen: 9
La opción ingresada no existe.
Seleccione el origen: hola
La opción ingresada no existe.
Seleccione el origen:
La opción ingresada no existe.
Seleccione el origen: 1
Seleccione el destino: 0
La opción ingresada no existe.
Seleccione el destino: 6

Ruta encontrada:

Mi casa -> Biblioteca -> Universidad -> Oficina de trabajo

Indicaciones:

1. Sal de Mi casa, gira a la izquierda y avanza dos cuadras por la Carrera 2.

2. Continúa por la Avenida Central tres cuadras hasta la Universidad.

3. Sal de la Universidad, gira a la derecha y avanza dos cuadras.

Número de lugares: 4
```

**Estado:** Correcta.

## Prueba 6: Buscar otra ruta (S/N)

**Entradas:** `3`, `5`, `s` (buscar otra ruta, en minúscula), `7`, `1`, `n` (terminar).

**Resultado esperado:** después de la primera ruta se vuelve a mostrar la lista de lugares; al responder `n` el programa termina. Se aceptan mayúsculas y minúsculas.

**Resultado obtenido:**

```text
Seleccione el origen: 3
Seleccione el destino: 5

Ruta encontrada:

Biblioteca -> Universidad

Indicaciones:

1. Continúa por la Avenida Central tres cuadras hasta la Universidad.

Número de lugares: 2

¿Desea buscar otra ruta? S/N s

Lugares disponibles:

1. Mi casa
2. Minimarket del barrio
3. Biblioteca
4. Estadio de fútbol
5. Universidad
6. Oficina de trabajo
7. Restaurante

Seleccione el origen: 7
Seleccione el destino: 1

Ruta encontrada:

Restaurante -> Estadio de fútbol -> Minimarket del barrio -> Mi casa

Indicaciones:

1. Desde el Restaurante avanza dos cuadras hacia el Estadio.

2. Toma la Calle del Parque y avanza tres cuadras hasta el Minimarket.

3. Sal del Minimarket, gira a la izquierda y regresa una cuadra por la Calle 1.

Número de lugares: 4

¿Desea buscar otra ruta? S/N n

Gracias por usar el sistema.
```

**Estado:** Correcta.

## Prueba 7 (adicional): Ruta inexistente

Con la red del ejercicio todos los lugares están conectados, por eso este mensaje no aparece con ninguna combinación del 1 al 7. Para comprobar la validación se ejecutó una copia de `main.py` con este cambio en la base de conocimiento (se quitó Restaurante de las conexiones de Estadio de fútbol y de Oficina de trabajo):

```python
    "Estadio de fútbol": ["Minimarket del barrio"],
    "Oficina de trabajo": ["Universidad"],
```

**Entradas:** origen `1`, destino `7`.

**Resultado esperado:** "No existe una ruta disponible."

**Resultado obtenido:**

```text
Seleccione el origen: 1
Seleccione el destino: 7

No existe una ruta disponible.
```

**Estado:** Correcta. Para repetir esta prueba se puede hacer el mismo cambio temporal en `main.py` y deshacerlo al terminar.

## Verificación adicional

Con un script auxiliar (no incluido en el proyecto) se revisaron automáticamente las 42 combinaciones de origen y destino diferentes. En todas, la ruta usa solo conexiones de la base de conocimiento, no repite lugares, tiene una indicación para cada tramo y usa la menor cantidad de conexiones posible.

En 6 combinaciones existen dos rutas con la misma cantidad mínima de conexiones. En esos casos el programa muestra la primera que encuentra la búsqueda:

| Origen -> Destino | Ruta que muestra el programa | Otra ruta con las mismas conexiones |
| --- | --- | --- |
| Minimarket del barrio -> Oficina de trabajo | Minimarket del barrio -> Biblioteca -> Universidad -> Oficina de trabajo | Minimarket del barrio -> Estadio de fútbol -> Restaurante -> Oficina de trabajo |
| Biblioteca -> Restaurante | Biblioteca -> Minimarket del barrio -> Estadio de fútbol -> Restaurante | Biblioteca -> Universidad -> Oficina de trabajo -> Restaurante |
| Estadio de fútbol -> Universidad | Estadio de fútbol -> Minimarket del barrio -> Biblioteca -> Universidad | Estadio de fútbol -> Restaurante -> Oficina de trabajo -> Universidad |
| Universidad -> Estadio de fútbol | Universidad -> Biblioteca -> Minimarket del barrio -> Estadio de fútbol | Universidad -> Oficina de trabajo -> Restaurante -> Estadio de fútbol |
| Oficina de trabajo -> Minimarket del barrio | Oficina de trabajo -> Universidad -> Biblioteca -> Minimarket del barrio | Oficina de trabajo -> Restaurante -> Estadio de fútbol -> Minimarket del barrio |
| Restaurante -> Biblioteca | Restaurante -> Estadio de fútbol -> Minimarket del barrio -> Biblioteca | Restaurante -> Oficina de trabajo -> Universidad -> Biblioteca |
