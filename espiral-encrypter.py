from encrypter import Encrypter
import pyfiglet 

# Objeto encargado de la enciptación
encripter = Encrypter()

# Titulo del programa
title = pyfiglet.figlet_format("Espiral Encripter", font = "slant" )
print(title)

# ----- Menu del programa ----- #
option = 0
while option < 3:
    # Opciones del menu
    option = int(input("\nElija una opción => 1:Encriptar -  2:Desencriptar - 3:Finalizar :\t"))
    
    # Opción para enciptar una frase
    if option == 1:
        print('\nECRIPTADO')
        speed = int(input("Indique la frecuencia de encriptado: "))
        # cambiamos la frecuencia del encriptador 
        encripter.spinner(speed)
        chars = input("Escriba su frase: ")
        # encriptamos la frase y devolvemos el hash
        encripter.encrypt(chars)
        option = 1

    # Opción para desenciptar un hash
    if option == 2:
        print('\nDESENCRIPTADO')
        speed = int(input("Indique la frecuencia de encriptado: "))
        # cambiamos la frecuencia del encriptador 
        encripter.spinner(speed)
        hash_encrypt = input("Ingrese su hash: ")
        # desencriptamos la frase a partir de un hash
        encripter.decrypt(hash_encrypt)
        option = 2

    # Opción para terminar la ejecución del programa
    if option == 3:
        print('\n------ Fin del programa -------\n')    
        option = 3




