from Graph import *

def CreateGraph_1():
    G = LoadGraphFromFile('graph_data.txt')  # Cargamos el gráfico desde el archivo
    return G

print("Probando el grafo...")
G = CreateGraph_1()

# Mostrar los nodos cargados
print("Nodos en el gráfico:")
for node in G.nodes:
    print(f"Nombre: {node.name}, Coordenadas: ({node.x}, {node.y})")

# Mostrar los segmentos cargados
print("Segmentos en el gráfico:")
for segment in G.segments:
    print(f"Segmento: {segment.name}, Origen: {segment.origin.name}, Destino: {segment.destination.name}, Costo: {segment.cost}")

G.Plot()
G.PlotNode("C")

n = G.GetClosest(15, 5)
print(n.name)  # La respuesta debe ser J
n = G.GetClosest(8, 19)
print(n.name)  # La respuesta debe ser B