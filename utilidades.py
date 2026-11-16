''' El archivo "utilidades.py" se crea para el funcionamiento
interno de la red de ciudades y algoritmos de grafos'''

#R1. Lista de adyacencia: {ciudad: [ciudad_vecina, distancia_km],...}

CARRETERAS = {
    ("Quito", "Ambato", 130),
    ("Quito", "Guayaquil", 420),
    ("Ambato", "Riobamba", 55),
    ("Riobamba", "Guayaquil", 200),
    ("Riobamba", "Macas", 160),
    ("Riobamba", "Cuenca", 230),
    ("Guayaquil", "Cuenca", 200),
    ("Cuenca", "Macas", 300),
    ("Cuenca", "Loja", 210)
}

def construir_red (carreteras = CARRETERAS):
    #Construye la lista de adyacencia
    grafo = {}
    for a, b, km in carreteras:
        grafo.setdefault(a, []).append(b, km)
        grafo.setdefault(b, []).append(a, km)
    return grafo

def grados(grafo):
    #R1. grados de cada ciudad - cantidad de vecinos directos
    return{ciudad: len(vecinos) for ciudad, vecinos in grafo.items()}


#R2. BFS propio por medio de cola FIFO

def bfs(grafo, origen):
    ''' Devuelve (escalas, padres)
    escalas: {ciudad: nro_de_escalas}; padres: para construir la ruta.
    BFS: cada nodo ingresa una vez y cada arista se revisa una vez'''

    escalas = {origen: 0}
    padres = {origen: None}
    cola = deque([origen])

    while cola:
        u = cola.popleft()
        for vecino, _km in grafo[u]:
            if vecino not in escalas:
                escalas [vecino] = escalas[u]+1
                padres [vecino] = u
                cola.append(vecino)
    return escalas, padres

def ruta_bfs (padres, destino):
    '''Recrea la ruta más corta'''
    if destino not in padres:
        return None
    ruta = []
    while destino is not None:
        ruta.append(destino)
        destino = padres[destino]
    return ruta[::-1]

# R3. Dijkstra previsto

def dijkstra(grafo, origen):

    dist = {ciudad: float('inf') for ciudad in grafo}
    dist[origen] = 0
    heap = [(0, origen)]  # cola de prioridad
    while heap:
        d, u = heapq.heappop(heap)  # el mas cercano pendiente
        if d > dist[u]:
            continue  # ya teniamos una ruta mejor
        for vecino, peso in grafo[u]:
            if dist[u] + peso < dist[vecino]:  # relajacion
                dist[vecino] = dist[u] + peso
                heapq.heappush(heap, (dist[vecino], vecino))
    return dist

def ruta_dijkstra(grafo, dist, origen, destino):
    """Reconstruye la ruta de menor km usando solo el diccionario de distancias
    (así no se modifica el Dijkstra provisto): se retrocede desde el destino
    buscando el vecino 'u' tal que dist[u] + peso == dist[actual]"""
    if dist.get(destino, float('inf')) == float('inf'):
        return None
    ruta = [destino]
    actual = destino
    while actual != origen:
        for vecino, peso in grafo[actual]:
            if dist[vecino] + peso == dist[actual]:
                ruta.append(vecino)
                actual = vecino
                break
    return ruta[::-1]

def km_de_ruta(grafo, ruta):
    """Suma los km de una ruta (lista de ciudades)"""
    total = 0
    for a, b in zip(ruta, ruta[1:]):
        total += next(km for v, km in grafo[a] if v == b)
    return total


def buscar_ciudad(grafo, texto):
    """Normaliza la entrada del usuario (mayúsculas/espacios)"""
    for ciudad in grafo:
        if ciudad.lower() == texto.strip().lower():
            return ciudad
    return None