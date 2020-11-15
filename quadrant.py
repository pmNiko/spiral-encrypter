class Quadrant:
    # recibe como parametro el largo     
    def __init__(self, large, name):
        self.items = []
        self.large = large
        self.name = name

    # recibe el array de characters a agregar y el indice de inicio
    def add(self, characters, start):
        for char in range(start,len(characters)):
            # agrega la cantidad de caracteres segun su largo
            if len(self.items) < self.large:
                self.items.append(characters[char])