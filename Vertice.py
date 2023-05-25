class Vertice:
    # Clase que define los vertices de la grafica
    def __init__(self, i):
        self.id = id
        self.adyacente = []
        self.visitado = False
        self.padre = None
        self.distancia = float("inf")

    def agregarAdyasente(self, v, p):
        if v not in self.adyacente:
            self.adyacente.append([v, p])
