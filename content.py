# Entidad encaragada del manejo de contenido de cadenas
class Content:  

    def __init__(self):
        self.char_list = []

    # metodo para convertir una cadena de caracteres en un array
    def parse(self, chars): 
        self.char_list = []       
        for char in chars:
            self.char_list.append(char.upper())
        return self.char_list
    
    # metodo encaragado de convertir un array en una cadena de caracteres
    def render_hash(self, array_chars):
        hash_list = ''.join(array_chars)
        return hash_list