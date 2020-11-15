from characters import Characters
from quadrant import Quadrant
import copy

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
        self.quadrant_1 = quadrant_1
        self.quadrant_2 = quadrant_2
        self.quadrant_3 = quadrant_3
        self.quadrant_4 = quadrant_4
        self.quadrant_5 = quadrant_5
        self.quadrant_6 = quadrant_6
        self.mix_1_2_3 = []
        self.quadrant_4_spin = []
        self.quadrant_5_spin = []
        self.quadrant_6_spin = []
    
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
        self.mix_1_2_3 = self.frequency(self.mix_1_2_3, speed)
        print(self.mix_1_2_3)
        self.quadrant_4_spin = self.frequency(self.quadrant_4.items.copy(), speed)
        print(self.quadrant_4_spin)
        self.quadrant_5_spin = self.frequency(self.quadrant_5.items.copy(), speed)
        print(self.quadrant_5_spin)
        self.quadrant_6_spin = self.frequency(self.quadrant_6.items.copy(), speed)
        print(self.quadrant_6_spin)
    
    def reset(self):
        self.mix_1_2_3 = []
        self.quadrant_4_spin = []
        self.quadrant_4_spin = []
        self.quadrant_4_spin = []
    
    def mix_quadrant(self):
        self.mix_1_2_3.extend(self.quadrant_1.items)
        self.mix_1_2_3.extend(self.quadrant_2.items)
        self.mix_1_2_3.extend(self.quadrant_3.items)
        return self.mix_1_2_3
    

        
        


# print('Base :',characters.data, ' cantidad de caracteres: ',len(characters.data))
# print(cuadrante_1.name, cuadrante_1.items, ' cantidad de caracteres: ',len(cuadrante_1.items))
# print(cuadrante_2.name, cuadrante_2.items, ' cantidad de caracteres: ',len(cuadrante_2.items))
# print(cuadrante_3.name, cuadrante_3.items, ' cantidad de caracteres: ',len(cuadrante_3.items))
# print(cuadrante_4.name, cuadrante_4.items, ' cantidad de caracteres: ',len(cuadrante_4.items))
# print(cuadrante_5.name, cuadrante_5.items, ' cantidad de caracteres: ',len(cuadrante_5.items))
# print(cuadrante_6.name, cuadrante_6.items, ' cantidad de caracteres: ',len(cuadrante_6.items))
