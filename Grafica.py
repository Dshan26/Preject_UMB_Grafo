from Vertice import Vertice
import networkx as nx
import matplotlib.pyplot as plt

class Grafica:
    # Clase que define los vertices de la grafica
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self, id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id)

    def agregarArista(self, a, b, p):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarAdyasente(b, p)
            self.vertices[b].agregarAdyasente(a, p)

    def imprimirGrafica(self):
        for v in self.vertices:
            print("la distancia del vértice: " + str(v) + "\tes" " " + str(
                self.vertices[v].distancia) + "\tllegando desde:  " + str(self.vertices[v].padre))

    # Recostruir el camino de comienzo a fin para saber por donde debemos pasar
    def camino(self, a, b):
        camino = []
        actual = b
        while actual != None:
            camino.insert(0, actual)
            actual = self.vertices[actual].padre
        return [camino, self.vertices[b].distancia]

    def minimo(self, lista):
        if len(lista) > 0:
            m = self.vertices[lista[0]].distancia
            v = lista[0]
            for e in lista:
                if m > self.vertices[e].distancia:
                    m = self.vertices[e].distancia
                    v = e
            return v

    def dijkstra(self, a):
        if a in self.vertices:
            self.vertices[a].distancia = 0
            actual = a
            noVisitados = []
            for v in self.vertices:
                if v != a:
                    self.vertices[v].distancia = float('inf')
                self.vertices[v].padre = None
                noVisitados.append(v)
            while len(noVisitados) > 0:
                for adyacente in self.vertices[actual].adyacente:
                    if self.vertices[adyacente[0]].visitado == False:
                        if self.vertices[actual].distancia + adyacente[1] < self.vertices[adyacente[0]].distancia:
                            self.vertices[adyacente[0]].distancia = self.vertices[actual].distancia + adyacente[1]
                            self.vertices[adyacente[0]].padre = actual

                self.vertices[actual].visitado = True
                noVisitados.remove(actual)

                actual = self.minimo(noVisitados)

            else:
                return False

    def visualizar_grafo(self):
        G = nx.Graph()
        edge_labels = {}
        for v in self.vertices:
            G.add_node(v)
            for ady in self.vertices[v].adyacente:
                G.add_edge(v, ady[0], weight=ady[1])
                edge_labels[(v, ady[0])] = ady[1]
        pos = nx.spring_layout(G)
        plt.title("\nGrafo\n")
        nx.draw_networkx(G, pos, with_labels=True)  # grafica aristas y vertices
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # muestra pesos en las aristas
        plt.show()

    def visualizar_dijkstra(self, start_node, end_node):

        plt.title("\nGrafo con Camino Dijkstra\n\n")

        # Construir el grafo G con los vertices y aristas originales
        G = nx.Graph()
        edge_labels = {}
        for v in self.vertices:

            for i, ady in enumerate(self.vertices[v].adyacente):
                destination_node = ady[0]
                weight = ady[1]
                G.add_edge(v, destination_node, weight=weight)  # muestra aristas
                edge_labels[(v, destination_node)] = f"{v} -> {(destination_node)}"  # muestra la direccion

        # Obtener el camino del inicio al final
        camino = self.camino(start_node, end_node)[0]

        # Crear lista de colores para las aristas
        edge_colors = ['black' if edge in zip(camino, camino[1:]) else 'red' for edge in G.edges()]

        # Obtener las coordenadas de los vertices para el trazado de la ruta
        node_positions = nx.spring_layout(G)

        # Dibujar el grafo original con los vertices y aristas
        nx.draw_networkx(G, pos=node_positions, with_labels=True, edge_color=edge_colors, width=2.0)
        nx.draw_networkx_edge_labels(G, pos=node_positions, edge_labels=edge_labels)

        # Trazar la ruta del algoritmo de Dijkstra
        for i in range(len(camino) - 1):
            plt.plot([node_positions[camino[i]][0], node_positions[camino[i + 1]][0]],
                     'r', linewidth=2)

