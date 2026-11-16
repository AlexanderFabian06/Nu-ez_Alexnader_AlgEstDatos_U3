'''Tarea 3
Progarama que me permite crear una red de ciudades, modelado, recorridos y ruta mínima'''

from utilidades import (construir_red, grados, bfs, ruta_bfs, dijkstra, ruta_dijkstra, km_de_ruta, buscar_ciudad)

RED = construir_red()

def pedir_ciudad (mensaje):
    ciudad = buscar_ciudad(RED,input(mensaje))
    if ciudad is None:
        print("Ciudad no encontrada. Escoger:", ",".join(RED))
    return ciudad

def r1_modelado():
    #Lista de adyacencia y grados
    print("\n R1: Lista de adyacencia ")
    for ciudad, vecinos in RED.items():
        print(f" {ciudad}: {vecinos}")
    for ciudad, g in RED.items():
        print(f" {ciudad}: {g}")

def r2_bfs():
    #BFS propio
    origen = pedir_ciudad("Ciudad origen: ")
    if not origen:
        return
    escalas, _=bfs(RED, origen)
    print(f"\n R2: Ciudades alcanzables desde {origen} ")
    for ciudad, n in sorted(escalas.items(), key = lambda x: x[1]):
        print(f" {ciudad}: {n} escalas (s)")
    aisladas = [c for c in RED if c not in escalas]
    if aisladas:
        print("La red no está completamente conectada. Desconectados: ", aisladas)
    else:
        print("La red está conectada en todos sus puntos.")


def r3_dijkstra():
    #Dijkstra proyectado. Cada relajación puede hacer un push o un pop
    origen = pedir_ciudad("Ciudad de origen: ")
    if not origen:
        return
    dist = dijkstra(RED, origen)
    print(f"\n R3: Distancia mínima en km desde el {origen}")
    for ciudad, d in sorted(dist.items(), key = lambda x : x[1]):
        print(f" {ciudad}; {d} km")
    alcanzables = {c: d for c, d in dist.items() if c != origen and d != float('inf')}
    if alcanzables:
        print("Ciudades más cercanas:", min(alcanzables, key = alcanzables.get),
              f"({min(alcanzables.values())} km)")

def r4_comparacion ():
    #Comparación BFS + Dijkstra
    origen = pedir_ciudad("Ciudad de origen: ")
    destino = pedir_ciudad("Ciudad de destino: ")
    if not origen or not destino:
        return
    escalas, padres = bfs (RED, origen)
    r_bfs = ruta_bfs(padres, destino)
    dist= dijkstra(RED, origen)
    r_dij = ruta_dijkstra(RED, dist, origen, destino)
    if r_bfs is None:
        print("No existe una rute entre esas ciudades")
        return
    print(f"\n R4: {origen} -> {destino}")
    print(f"Menos escalas (BFS)  : {' -> '.join(r_bfs)} | "
          f"{escalas[destino]} escala(s) | {km_de_ruta(RED, r_bfs)} km")
    print(f"Menor distancia (Dij): {' -> '.join(r_dij)} | "
          f"{len(r_dij) - 1} escala(s) | {dist[destino]} km")
    if r_bfs == r_dij:
        print("Ambas rutas coinciden")
    else:
        print("Las rutas no coinciden: aunque haya pocas escalas, los km son mayores")


def menu():
    opciones = {"1": r1_modelado, "2": r2_bfs, "3": r3_dijkstra, "4": r4_comparacion}
    while True:
        print("\n RED DE CIUDADES ")
        print("1. R1 Modelado y grados \n2. R2 Recorrido BFS\n" \
        "3. R3 Ruta mínima (Dijkstra\n 4. R4 Comparación BFS vs Dijkstra\n 0. Salir.)")
        op = input("opción: ").strip()
        if op == "0":
            break
        opciones.get(op, lambda: print("Opción inválida"))()


if __name__=="__main:__":
    menu()

    