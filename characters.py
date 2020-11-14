import random

abc = [
        '-', 
        '*', 
        '1', ' ', 
        'H', 'B', '+', 
        '!', 'M', 'C', '?', 'Y', 
        '.', 'F', '2', '7', 'R', 'G', '6', '0', 
        'D', 'U', 'K', 'T', ')', '#', '@', '8', 'Q', '/', '%', 'P', 'I', 
        '5', 'S', 'J', '$', 'A', '3', 'O', '9', 'X', 'V', 'E', '=', 'L', 'Z', 'N', '(', '"', '4', 'Ñ', 'W', ','
        ]

class Characters:  

    def __init__(self):
        self.data = abc

    def position(self):
        for item in self.data:
            print('Posición ',self.data.index(item)+1, ' -> ', item )

    def mixed(self):
        mix_characters = random.sample(self.data,54)
        return mix_characters
        

