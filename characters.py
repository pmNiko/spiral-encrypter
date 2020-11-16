import random

# Este es el rango de caracteres validos a utlizar
items = [
        '-', '*', 
        '1', ' ', 'H', 
        'B', '+','!', 'M', 'C', 
        '?', 'Y', '.', 'F', '2', '7', 'R', 'G', 
        '6', '0', 'D', 'U', 'K', 'T', ')', ',', '@', '8', 'Q', '/', '%', 
        'P', 'I', '5', 'S', 'J', '$', 'A', '3', 'O', '9', 'X', 'V', 'E', '=', 'L', 'Z', 'N', '(', '"', '4', 'W'
        ]

# Entidad encargada del manejo del rango de caracteres base
class Characters:  

    def __init__(self):
        self.chars = items
        
    # cantidad de caracteres contenidos
    def large(self):
        return len(self.chars)

    # devuelve la posición de un caracter 
    def position(self, char):
        return self.chars.index(char)

    # imprime la posición de todos los caracteres
    def render_positions(self):
        for item in self.chars:
            print('Posición ', self.position(item), ' -> ', item )

    # devuelve un array random de los caracteres
    def mixed(self):
        return random.sample(self.chars, 52)
        
        

