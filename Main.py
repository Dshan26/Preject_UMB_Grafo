# Definir vertices, aritas y pesos de la aristas
import networkx as nx
from matplotlib import pyplot as plt

from Grafica import Grafica


class main:
    G = nx.DiGraph()
    g = Grafica()
    g.agregarVertice(1)
    g.agregarVertice(2)
    g.agregarVertice(3)
    g.agregarVertice(4)
    g.agregarVertice(5)
    g.agregarVertice(6)
    g.agregarVertice(7)
    g.agregarVertice(8)
    g.agregarArista(1, 2, 9.156)
    g.agregarArista(1, 3, 5.9)
    g.agregarArista(1, 4, 13.7)
    g.agregarArista(1, 3, 1.08)
    g.agregarArista(1, 6, 13.3)
    g.agregarArista(1, 7, 4.2)
    g.agregarArista(1, 8, 18.07)
    g.agregarArista(1, 6, 3.35)
    g.agregarArista(1, 5, 12.5)

    start_node = 1
    end_node = 8

    print("La ruta más corta según el algoritmo de DIJKSTRA y según su peso es: \n")
    g.dijkstra(1)  # muestra el camino
    print(g.camino(1, 8))

    print("\nValores de la gráfica:\n")
    g.visualizar_grafo()
    plt.title("\n\nCamino Dijkstra\n")
    g.dijkstra(start_node)
    g.visualizar_dijkstra(start_node, end_node)