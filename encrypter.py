from characters import Characters
from quadrant import Quadrant
import copy
from content import Content

# creación de una instancia de Characters
characters = Characters()
# creación de los cuadrantes del espiral 
# con la capacidad de items a contener y un nombre
quadrant_1 = Quadrant( 2,  'Primer Cuadrante' )
quadrant_2 = Quadrant( 3,  'Segundo Cuadrante')
quadrant_3 = Quadrant( 5,  'Tercero Cuadrante')
quadrant_4 = Quadrant( 8,  'Cuarto Cuadrante' )
quadrant_5 = Quadrant( 13, 'Quinto Cuadrante' )
quadrant_6 = Quadrant( 21, 'Sexto Cuadrante'  )
# le proveemos a los cuadrantes el array de caracteres base
# y le indicamos a partir de que indice comenzar agregarlos
quadrant_1.add( characters.chars, 0 )
quadrant_2.add( characters.chars, 2 )
quadrant_3.add( characters.chars, 5 )
quadrant_4.add( characters.chars, 10)
quadrant_5.add( characters.chars, 18)
quadrant_6.add( characters.chars, 31)

class Encrypter:
    
    def __init__(self):
        self.content = Content()
        self.quadrant_1 = quadrant_1
        self.quadrant_2 = quadrant_2
        self.quadrant_3 = quadrant_3
        self.quadrant_4 = quadrant_4
        self.quadrant_5 = quadrant_5
        self.quadrant_6 = quadrant_6
        self.mix_1_2_3 = []
        self.chars_spiral = []
        self.quadrant_4_spin = []
        self.quadrant_5_spin = []
        self.quadrant_6_spin = []
        self.chars_spin = []
    
    def encrypt(self, chars):
        array_chars = self.content.parse(chars)
        hash_encrypt = []
        for char in array_chars:
            if char in self.chars_spiral:
                poistion = self.chars_spiral.index(char)
                hash_encrypt.append(self.chars_spin[poistion])
            else:
                hash_encrypt.append('#')
        your_hash = self.content.render_hash(hash_encrypt)
        print('Su hash => ', your_hash)
    
    def decrypt(self, hash_encrypt):
        array_chars = self.content.parse(hash_encrypt)
        hash_decrypt = []
        for char in array_chars:
            if char in self.chars_spin:
                poistion = self.chars_spin.index(char)
                hash_decrypt.append(self.chars_spiral[poistion])
            else:
                hash_decrypt.append('#')
        your_phrase = self.content.render_hash(hash_decrypt)
        print('Su frase es => ', your_phrase)
    
    # gira la posición de los caracteres segun el speed
    def frequency(self, items, speed):
        # bandera de velocidad
        velocity = 0
        for char in items:
            if velocity < speed:
                char = items.pop(0)
                items.append(char)
            velocity += 1
        return items

    def spinner(self, speed):
        self.reset()
        self.mix_quadrant()
        self.set_chars_spiral()

        self.mix_1_2_3 = self.frequency(self.mix_1_2_3, speed)
        self.quadrant_4_spin = self.frequency(self.quadrant_4.items.copy(), speed)
        self.quadrant_5_spin = self.frequency(self.quadrant_5.items.copy(), speed)
        self.quadrant_6_spin = self.frequency(self.quadrant_6.items.copy(), speed)

        self.chars_spin.extend(self.mix_1_2_3.copy())
        self.chars_spin.extend(self.quadrant_4_spin.copy())
        self.chars_spin.extend(self.quadrant_5_spin.copy())
        self.chars_spin.extend(self.quadrant_6_spin.copy())
    
    def set_chars_spiral(self):
        self.chars_spiral.extend(self.mix_1_2_3.copy())
        self.chars_spiral.extend(self.quadrant_4.items.copy())
        self.chars_spiral.extend(self.quadrant_5.items.copy())
        self.chars_spiral.extend(self.quadrant_6.items.copy())
    
    def mix_quadrant(self):
        self.mix_1_2_3.extend(self.quadrant_1.items.copy())
        self.mix_1_2_3.extend(self.quadrant_2.items.copy())
        self.mix_1_2_3.extend(self.quadrant_3.items.copy())
        return self.mix_1_2_3

    def reset(self):
        self.mix_1_2_3 = []
        self.quadrant_4_spin = []
        self.quadrant_4_spin = []
        self.quadrant_4_spin = []
        self.chars_spin = []
        self.chars_spiral = []
    
    

        
        


# print('Base :',characters.data, ' cantidad de caracteres: ',len(characters.data))
# print(cuadrante_1.name, cuadrante_1.items, ' cantidad de caracteres: ',len(cuadrante_1.items))
# print(cuadrante_2.name, cuadrante_2.items, ' cantidad de caracteres: ',len(cuadrante_2.items))
# print(cuadrante_3.name, cuadrante_3.items, ' cantidad de caracteres: ',len(cuadrante_3.items))
# print(cuadrante_4.name, cuadrante_4.items, ' cantidad de caracteres: ',len(cuadrante_4.items))
# print(cuadrante_5.name, cuadrante_5.items, ' cantidad de caracteres: ',len(cuadrante_5.items))
# print(cuadrante_6.name, cuadrante_6.items, ' cantidad de caracteres: ',len(cuadrante_6.items))
