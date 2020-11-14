from alphabet import Alphabet
from quadrant import Quadrant

print("FLOGRAMA HASH")
# name = input("Ingrese su nombre ")
# print("\n")
# print("Bienvenido ", name)

alf = Alphabet()
# vector = alf.data

cuadrante_1 = Quadrant(1,0,'Primer Cuadrante')
cuadrante_2 = Quadrant(1,1,'Segundo Cuadrante')
cuadrante_3 = Quadrant(2,2,'Tercero Cuadrante')
cuadrante_4 = Quadrant(3,4,'Cuarto Cuadrante')
cuadrante_5 = Quadrant(5,7,'Quinto Cuadrante')
cuadrante_6 = Quadrant(8,12,'Sexto Cuadrante')
cuadrante_7 = Quadrant(13,20,'Septimo Cuadrante')
cuadrante_8 = Quadrant(21,33,'Octavo Cuadrante')

cuadrante_1.add(alf.data)
cuadrante_2.add(alf.data)
cuadrante_3.add(alf.data)
cuadrante_4.add(alf.data)
cuadrante_5.add(alf.data)
cuadrante_6.add(alf.data)
cuadrante_7.add(alf.data)
cuadrante_8.add(alf.data)

print(cuadrante_1.name, cuadrante_1.items)
print(cuadrante_2.name, cuadrante_2.items)
print(cuadrante_3.name, cuadrante_3.items)
print(cuadrante_4.name, cuadrante_4.items)
print(cuadrante_5.name, cuadrante_5.items)
print(cuadrante_6.name, cuadrante_6.items)
print(cuadrante_7.name, cuadrante_7.items)
print(cuadrante_8.name, cuadrante_8.items)

# for x in range(5,len(alf.data)):
#     print(alf.data[x])
