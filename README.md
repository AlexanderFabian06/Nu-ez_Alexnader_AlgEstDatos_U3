*** Tarea 3. Red de ciudades: modelado, recorridos y ruta mínima ***
**Deber de la Unidad 3**

*Guía de Ejecución*
Requiere Python (sin librerías externas).

bash
python main.py

La red de ejemplo (7 ciudades del Ecuador, grafo no dirigido y ponderado en km) ya viene cargada.

Archivos
main.py: menú de consola y los cuatro requerimientos.
utilidades.py: construcción de la red, BFS propio, Dijkstra provisto y funciones auxiliares.
Requerimientos
Req.	Qué hace	Complejidad
R1	Muestra la lista de adyacencia y el grado de cada ciudad	O(V + E)
R2	BFS desde un origen: escalas a cada ciudad e indica si la red es conexa	O(V + E)
R3	Dijkstra (provisto): distancia mínima en km, ciudad más cercana y más lejana	O((V + E) log V)
R4	Compara la ruta con menos escalas (BFS) vs la de menos km (Dijkstra)	O((V + E) log V)

Ejemplo R4: Quito -> Guayaquil. BFS: Quito -> Guayaquil (1 escala, 420 km). Dijkstra: Quito -> Ambato -> Riobamba -> Guayaquil (3 escalas, 385 km).
