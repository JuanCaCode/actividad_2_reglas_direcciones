# Sistema Inteligente de Rutas

Actividad 2 del curso de Introducción a la Inteligencia Artificial (Universidad Iberoamericana): sistemas basados en conocimiento y búsqueda de rutas.

## Objetivo

Crear un programa sencillo en Python, que funciona desde la terminal, en el que el usuario selecciona un lugar de origen y un lugar de destino. El sistema busca una ruta entre ambos y muestra:

1. La ruta encontrada.
2. Los lugares por los que debe pasar.
3. Las indicaciones para ir de un lugar al siguiente.
4. La cantidad de lugares que componen la ruta.

## Base de conocimiento

El conocimiento está escrito en `main.py`, separado del algoritmo que lo usa:

- Variables de los lugares (`CASA`, `MINIMARKET`, `BIBLIOTECA`, `ESTADIO`, `UNIVERSIDAD`, `OFICINA` y `RESTAURANTE`): cada nombre se escribe una sola vez y el resto del código usa la variable. Si un lugar cambia de nombre, solo se modifica su variable (y, si hace falta, el texto de sus indicaciones).
- `lugares`: el menú, que relaciona cada número del 1 al 7 con su lugar.
- `conexiones`: diccionario con los lugares conectados directamente con cada lugar (los **hechos**).
- `indicaciones`: las **reglas de dirección**. La clave es una tupla `(desde, hasta)`, por ejemplo `(CASA, BIBLIOTECA)`, y el valor es la indicación de ese tramo. Por ejemplo: *si* se va de Mi casa a Biblioteca, *entonces* "Sal de Mi casa, gira a la izquierda y avanza dos cuadras por la Carrera 2."

Hay 8 conexiones de doble sentido, por eso hay 16 reglas de dirección (una para cada sentido):

```text
Mi casa ------------ Minimarket del barrio ------ Estadio de fútbol
   |                           |                          |
Biblioteca --------------------+                          |
   |                                                      |
Universidad ------ Oficina de trabajo -------------- Restaurante
```

Las direcciones son ficticias y solamente representan las reglas de la base de conocimiento del ejercicio.

## Estrategia de búsqueda

Se usa **búsqueda en anchura** (BFS, *Breadth-First Search*) en la función `buscar_ruta`:

1. Una lista guarda las rutas pendientes. Al inicio solo contiene la ruta `[origen]`.
2. Se toma la primera ruta de la lista.
3. Se revisa el último lugar de esa ruta.
4. Si es el destino, se retorna la ruta.
5. Si no es el destino, se revisan sus conexiones.
6. Con cada lugar conectado que todavía no se ha visitado se crea una nueva posible ruta, que se agrega al final de la lista.
7. Se continúa hasta encontrar el destino. Si la lista queda vacía, no existe una ruta.

La lista `visitados` evita revisar dos veces el mismo lugar.

Ejemplo paso a paso de **Mi casa -> Restaurante**:

| Paso | Ruta que se toma de la lista | ¿Es el destino? | Nuevas rutas que se agregan |
| --- | --- | --- | --- |
| 1 | Mi casa | No | Mi casa -> Minimarket del barrio y Mi casa -> Biblioteca |
| 2 | Mi casa -> Minimarket del barrio | No | Mi casa -> Minimarket del barrio -> Estadio de fútbol |
| 3 | Mi casa -> Biblioteca | No | Mi casa -> Biblioteca -> Universidad |
| 4 | Mi casa -> Minimarket del barrio -> Estadio de fútbol | No | Mi casa -> Minimarket del barrio -> Estadio de fútbol -> Restaurante |
| 5 | Mi casa -> Biblioteca -> Universidad | No | Mi casa -> Biblioteca -> Universidad -> Oficina de trabajo |
| 6 | Mi casa -> Minimarket del barrio -> Estadio de fútbol -> Restaurante | **Sí** | Se retorna esta ruta |

## ¿Qué significa "mejor ruta"?

La mejor ruta es **la ruta que utiliza la menor cantidad de conexiones entre los lugares**.

La búsqueda en anchura revisa primero todas las rutas de 1 conexión, después las de 2, después las de 3, y así sucesivamente. Por eso la primera ruta que llega al destino es la más corta. En el ejemplo anterior, la ruta por Minimarket del barrio y Estadio de fútbol usa 3 conexiones, y la ruta por Biblioteca, Universidad y Oficina de trabajo usaría 4.

Si dos rutas tienen la misma cantidad de conexiones, se muestra la primera que encuentra la búsqueda.

## Requisitos

- Python 3.7 o superior (probado con Python 3.14.7).
- No tiene dependencias externas: no hay que instalar nada.

## Cómo ejecutar

Desde la carpeta del proyecto:

```bash
python main.py
```

En algunos sistemas el comando es `python3 main.py`. El origen y el destino se eligen escribiendo un número del 1 al 7.

## Ejemplo de ejecución

```text
========================================
       SISTEMA INTELIGENTE DE RUTAS
========================================

Lugares disponibles:

1. Mi casa
2. Minimarket del barrio
3. Biblioteca
4. Estadio de fútbol
5. Universidad
6. Oficina de trabajo
7. Restaurante

Seleccione el origen: 1
Seleccione el destino: 7

Ruta encontrada:

Mi casa -> Minimarket del barrio -> Estadio de fútbol -> Restaurante

Indicaciones:

1. Sal de Mi casa, gira a la derecha y avanza una cuadra por la Calle 1.

2. Toma la Calle del Parque y avanza tres cuadras hasta el Estadio.

3. Rodea el Estadio por el costado oriental y avanza dos cuadras.

Número de lugares: 4

¿Desea buscar otra ruta? S/N N

Gracias por usar el sistema.
```
