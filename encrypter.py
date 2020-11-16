from characters import Characters
from quadrant import Quadrant
import copy
from content import Content

# creación de una instancia de Characters
characters = Characters()
# creación de los cuadrantes del espiral 
# con la capacidad de items a contener
quadrant_1 = Quadrant(2)
quadrant_2 = Quadrant(3)
quadrant_3 = Quadrant(5)
quadrant_4 = Quadrant(8)
quadrant_5 = Quadrant(13)
quadrant_6 = Quadrant(21)
# le proveemos a los cuadrantes el array de caracteres base
# y le indicamos a partir de que indice comenzar agregarlos
quadrant_1.add( characters.chars, 0 )
quadrant_2.add( characters.chars, 2 )
quadrant_3.add( characters.chars, 5 )
quadrant_4.add( characters.chars, 10)
quadrant_5.add( characters.chars, 18)
quadrant_6.add( characters.chars, 31)

# Entidad encargada de la enciptación y desencriptación de frases
class Encrypter:
    
    def __init__(self):
        # objeto para manejo de contenido
        self.content = Content()
        # cuadrantes que manejará
        self.quadrant_1 = quadrant_1
        self.quadrant_2 = quadrant_2
        self.quadrant_3 = quadrant_3
        self.quadrant_4 = quadrant_4
        self.quadrant_5 = quadrant_5
        self.quadrant_6 = quadrant_6
        # array de los cuadrantes 1, 2 y 3
        self.mix_1_2_3 = []
        # cuandrantes en frecuencia
        self.quadrant_4_spin = []
        self.quadrant_5_spin = []
        self.quadrant_6_spin = []        
        # array con los items de los 6 cuadrantes
        self.chars_spiral = []
        # chars_spiral en frecuencia
        self.chars_spin = []
    
    # ---- Metodo principal de encriptado ----- #
    def encrypt(self, chars):
        # convierte la cadena de chars en un array
        array_chars = self.content.parse(chars)
        hash_encrypt = []
        for char in array_chars:
            # corrobora que el caracter sea valido 
            if char in self.chars_spiral:
                # recupera la posición en el array del espiral
                poistion = self.chars_spiral.index(char)
                # agrega el caracter encriptado al hash 
                hash_encrypt.append(self.chars_spin[poistion])
            else:
                # si el caracter es invalido agrega un #
                hash_encrypt.append('#')
        # imprime el hash correspondiente a la frase
        print('Su hash => ', self.content.render_hash(hash_encrypt))
    
    # ---- Metodo principal de desencriptado ----- #
    def decrypt(self, hash_encrypt):
        array_chars = self.content.parse(hash_encrypt)
        hash_decrypt = []
        for char in array_chars:
            if char in self.chars_spin:
                # recupera la posición del caracter encriptado
                poistion = self.chars_spin.index(char)
                hash_decrypt.append(self.chars_spiral[poistion])
            else:
                hash_decrypt.append('#')
        # imprime la frase desencriptada 
        print('Su frase es => ', self.content.render_hash(hash_decrypt))
    
    # rota la posición de los caracteres 
    # que recibe como parametro segun el speed
    def frequency(self, items, speed):
        # bandera de velocidad
        velocity = 0
        for char in items:
            if velocity < speed:
                char = items.pop(0)
                items.append(char)
            velocity += 1
        return items

    # metodo para poner en frecuencia los cuadrantes 
    # del encriptador
    def spinner(self, speed):
        self.reset()
        self.mix_quadrant()
        self.set_chars_spiral()
        # contiene la frecuencia de los cuadrantes
        self.mix_1_2_3 = self.frequency(self.mix_1_2_3, speed)
        self.quadrant_4_spin = self.frequency(self.quadrant_4.items.copy(), speed)
        self.quadrant_5_spin = self.frequency(self.quadrant_5.items.copy(), speed)
        self.quadrant_6_spin = self.frequency(self.quadrant_6.items.copy(), speed)
        # contiene los cuadrantes en frecuencia
        self.chars_spin.extend(self.mix_1_2_3.copy())
        self.chars_spin.extend(self.quadrant_4_spin.copy())
        self.chars_spin.extend(self.quadrant_5_spin.copy())
        self.chars_spin.extend(self.quadrant_6_spin.copy())
    
    # metodo para contener los caracteres de todos los cuadrantes 
    def set_chars_spiral(self):
        self.chars_spiral.extend(self.mix_1_2_3.copy())
        self.chars_spiral.extend(self.quadrant_4.items.copy())
        self.chars_spiral.extend(self.quadrant_5.items.copy())
        self.chars_spiral.extend(self.quadrant_6.items.copy())
    
    # metodo para contener los caracteres de los cuadrantes 1, 2 y 3
    def mix_quadrant(self):
        self.mix_1_2_3.extend(self.quadrant_1.items.copy())
        self.mix_1_2_3.extend(self.quadrant_2.items.copy())
        self.mix_1_2_3.extend(self.quadrant_3.items.copy())

    # metodo para resetear los array de apoyo
    def reset(self):
        self.mix_1_2_3 = []
        self.quadrant_4_spin = []
        self.quadrant_4_spin = []
        self.quadrant_4_spin = []
        self.chars_spin = []
        self.chars_spiral = []