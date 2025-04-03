from Graph import *

def CreateGraph_1():
    G = Graph()
    G.AddNode(Node("A", 1, 20))
    G.AddNode(Node("B", 8, 17))
    G.AddNode(Node("C", 15, 20))
    G.AddNode(Node("D", 18, 15))
    G.AddNode(Node("E", 2, 4))
    G.AddNode(Node("F", 6, 5))
    G.AddNode(Node("G", 12, 12))
    G.AddNode(Node("H", 10, 3))
    G.AddNode(Node("I", 19, 1))
    G.AddNode(Node("J", 13, 5))
    G.AddNode(Node("K", 3, 15))
    G.AddNode(Node("L", 4, 10))
    G.AddSegment("AB", "A", "B")
    G.AddSegment("AE", "A", "E")
    G.AddSegment("AK", "A", "K")
    G.AddSegment("BA", "B", "A")
    G.AddSegment("BC", "B", "C")
    G.AddSegment("BF", "B", "F")
    G.AddSegment("BK", "B", "K")
    G.AddSegment("BG", "B", "G")
    G.AddSegment("CD", "C", "D")
    G.AddSegment("CG", "C", "G")
    G.AddSegment("DG", "D", "G")
    G.AddSegment("DH", "D", "H")
    G.AddSegment("DI", "D", "I")
    G.AddSegment("EF", "E", "F")
    G.AddSegment("FL", "F", "L")
    G.AddSegment("GB", "G", "B")
    G.AddSegment("GF", "G", "F")
    G.AddSegment("GH", "G", "H")
    G.AddSegment("ID", "I", "D")
    G.AddSegment("IJ", "I", "J")
    G.AddSegment("JI", "J", "I")
    G.AddSegment("KA", "K", "A")
    G.AddSegment("KL", "K", "L")
    G.AddSegment("LK", "L", "K")
    G.AddSegment("LF", "L", "F")

    return G


def CreateGraph_2():
    G = Graph()

    # Añadir nodos al grafo
    G.AddNode(Node("M", 2, 3))
    G.AddNode(Node("N", 5, 8))
    G.AddNode(Node("O", 10, 2))
    G.AddNode(Node("P", 7, 10))
    G.AddNode(Node("Q", 4, 6))
    G.AddNode(Node("R", 8, 3))

    # Añadir segmentos (conexiones entre nodos)
    G.AddSegment("MN", "M", "N")
    G.AddSegment("MO", "M", "O")
    G.AddSegment("NP", "N", "P")
    G.AddSegment("NQ", "N", "Q")
    G.AddSegment("RQ", "R", "Q")
    G.AddSegment("OR", "O", "R")
    G.AddSegment("OP", "O", "P")

    return G


# Llamada a la función CreateGraph_1
print("Probando el grafo 1...")
G1 = CreateGraph_1()
G1.Plot()
plt.show()

# Mostrar el grafo 1 y los vecinos de C
G1.PlotNode("C")

# Prueba de la función GetClosest en el primer grafo
n = G1.GetClosest(15, 5)
print(n.name)  # La respuesta debe ser J

n = G1.GetClosest(8, 19)
print(n.name)  # La respuesta debe ser B

# Llamada a la función CreateGraph_2
print("Probando el grafo 2...")
G2 = CreateGraph_2()
G2.Plot()
plt.show()

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