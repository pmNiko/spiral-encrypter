from characters import Characters
from quadrant import Quadrant

characters = Characters()

cuadrante_1 = Quadrant(1,0,'Primer Cuadrante')
cuadrante_2 = Quadrant(1,1,'Segundo Cuadrante')
cuadrante_3 = Quadrant(2,2,'Tercero Cuadrante')
cuadrante_4 = Quadrant(3,4,'Cuarto Cuadrante')
cuadrante_5 = Quadrant(5,7,'Quinto Cuadrante')
cuadrante_6 = Quadrant(8,12,'Sexto Cuadrante')
cuadrante_7 = Quadrant(13,20,'Septimo Cuadrante')
cuadrante_8 = Quadrant(21,33,'Octavo Cuadrante')

cuadrante_1.add(characters.data)
cuadrante_2.add(characters.data)
cuadrante_3.add(characters.data)
cuadrante_4.add(characters.data)
cuadrante_5.add(characters.data)
cuadrante_6.add(characters.data)
cuadrante_7.add(characters.data)
cuadrante_8.add(characters.data)

class Encriptor:
    
    def __init__(self):
        self.cuadrante_1 = cuadrante_1
        self.cuadrante_2 = cuadrante_2
        self.cuadrante_3 = cuadrante_3
        self.cuadrante_4 = cuadrante_4
        self.cuadrante_5 = cuadrante_5
        self.cuadrante_6 = cuadrante_6
        self.cuadrante_7 = cuadrante_7
        self.cuadrante_8 = cuadrante_8
    
    def frecquency(self, quadrant,speed):
        velocity = 0
        print(quadrant.items)
        for char in quadrant.items:
            if velocity < speed:
                char = quadrant.items.pop(0)
                print(char)
                print(quadrant.items)
                quadrant.items.append(char)
                print(quadrant.items)
            velocity += 1

enc = Encriptor()
un_cuadrante = enc.cuadrante_5
enc.frecquency(un_cuadrante,3)





# print('Base :',characters.data, ' cantidad de caracteres: ',len(characters.data))
# print(cuadrante_1.name, cuadrante_1.items, ' cantidad de caracteres: ',len(cuadrante_1.items))
# print(cuadrante_2.name, cuadrante_2.items, ' cantidad de caracteres: ',len(cuadrante_2.items))
# print(cuadrante_3.name, cuadrante_3.items, ' cantidad de caracteres: ',len(cuadrante_3.items))
# print(cuadrante_4.name, cuadrante_4.items, ' cantidad de caracteres: ',len(cuadrante_4.items))
# print(cuadrante_5.name, cuadrante_5.items, ' cantidad de caracteres: ',len(cuadrante_5.items))
# print(cuadrante_6.name, cuadrante_6.items, ' cantidad de caracteres: ',len(cuadrante_6.items))
# print(cuadrante_7.name, cuadrante_7.items, ' cantidad de caracteres: ',len(cuadrante_7.items))
# print(cuadrante_8.name, cuadrante_8.items, ' cantidad de caracteres: ',len(cuadrante_8.items))
