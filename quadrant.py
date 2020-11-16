# Entidad encargada del manejo de los cuadrantes del espiral
class Quadrant:
    # recibe como parametro el largo     
    def __init__(self, large):
        self.items = []
        self.large = large

    # recibe el array de characters a agregar y el indice de inicio
    def add(self, characters, start):
        for char in range(start,len(characters)):
            # agrega la cantidad de caracteres segun su largo
            if len(self.items) < self.large:
                self.items.append(characters[char])