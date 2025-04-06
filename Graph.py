import matplotlib.pyplot as plt
import math
from node import Node, Distance
from segment import Segment


class Graph:
    def __init__(self):
        self.nodes = []
        self.segments = []

    def AddNode(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            return True
        return False

    def AddSegment(self, name, nameOrigin, nameDestination):
        origin_node = None
        destination_node = None

        # Encuentra los nodos por su nombre
        for node in self.nodes:
            if node.name == nameOrigin:
                origin_node = node
            if node.name == nameDestination:
                destination_node = node

        # Si ambos nodos se encuentran, se crea el segmento
        if origin_node and destination_node:
            segment = Segment(name, origin_node, destination_node)
            self.segments.append(segment)
            origin_node.add_neighbor(destination_node)  # Añade destino como vecino de origen
            return True
        return False

    def GetClosest(self, x, y):
        return min(self.nodes, key=lambda node: Distance(node, Node("temp", x, y)))

    def Plot(self):
        plt.figure(figsize=(8, 6))
        for segment in self.segments:
            x_values = [segment.origin.x, segment.destination.x]
            y_values = [segment.origin.y, segment.destination.y]
            plt.plot(x_values, y_values, color='blue' , linewidth=1)

            mid_x = (segment.origin.x + segment.destination.x) / 2
            mid_y = (segment.origin.y + segment.destination.y) / 2
            plt.text(mid_x, mid_y, f"{segment.cost:.1f}", fontsize=12, color='black')

        for node in self.nodes:
            plt.scatter(node.x, node.y, color='red', s=100)
            plt.text(node.x, node.y, node.name, fontsize=12, ha='right', color='green')

        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.title("Graph Representation")
        plt.show()

    def PlotNode(self, nameOrigin):
        origin = next((node for node in self.nodes if node.name == nameOrigin), None)
        if origin is None:
            return False

        plt.figure(figsize=(8, 6))

        for segment in self.segments:
            x_values = [segment.origin.x, segment.destination.x]
            y_values = [segment.origin.y, segment.destination.y]
            plt.plot(x_values, y_values, 'k-', linewidth=1)

            mid_x = (segment.origin.x + segment.destination.x) / 2
            mid_y = (segment.origin.y + segment.destination.y) / 2
            plt.text(mid_x, mid_y, f"{segment.cost:.1f}", fontsize=12, color='blue')

        for node in self.nodes:
            color = 'grey'
            if node == origin:
                color = 'blue'
            elif node in origin.neighbors:
                color = 'green'
            plt.scatter(node.x, node.y, color=color, s=100)
            plt.text(node.x, node.y, node.name, fontsize=12, ha='right')

        for neighbor in origin.neighbors:
            plt.plot([origin.x, neighbor.x], [origin.y, neighbor.y], 'r-', linewidth=2)

        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.title(f"Graph Representation Highlighting {nameOrigin}")
        plt.show()

        return True

def LoadGraphFromFile(filename):
    G = Graph()  # Creamos un nuevo objeto Graph
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            # Primero, procesamos los nodos
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) == 3:  # Formato del nodo: Nombre,X,Y
                    try:
                        node_name = parts[0]
                        x = float(parts[1])
                        y = float(parts[2])
                        G.AddNode(Node(node_name, x, y))
                    except ValueError:
                        # Si no se puede convertir x o y a float, se ignora la línea
                        continue
                elif len(parts) == 3 and parts[
                    0] != '':  # Formato de los segmentos: NombreSegmento,NodoOrigen,NodoDestino
                    segment_name = parts[0]
                    origin = parts[1]
                    destination = parts[2]
                    G.AddSegment(segment_name, origin, destination)
    except FileNotFoundError:
        print(f"Error: El archivo {filename} no se encuentra.")
    return G

def RemoveNode(self, name):
    self.nodes = [n for n in self.nodes if n.name != name]
    self.segments = [s for s in self.segments if s.origin.name != name and s.destination.name != name]

def SaveToFile(self, filename):
    with open(filename, 'w') as f:
        for node in self.nodes:
            f.write(f"{node.name} {node.x} {node.y}\n")
        f.write("SEGMENTS\n")
        for seg in self.segments:
            f.write(f"{seg.name} {seg.origin.name} {seg.destination.name} {seg.cost}\n")

@staticmethod
def LoadFromFile(filename):
    G = Graph()
    with open(filename, 'r') as f:
        lines = f.readlines()
    i = 0
    while i < len(lines) and lines[i].strip() != "SEGMENTS":
        name, x, y = lines[i].split()
        G.AddNode(Node(name, float(x), float(y)))
        i += 1
    i += 1
    while i < len(lines):
        name, origin, dest, *rest = lines[i].split()
        G.AddSegment(name, origin, dest)
        i += 1
    return G
