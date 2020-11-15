from encrypter import Encrypter
import pyfiglet 

encripter = Encrypter()

title = pyfiglet.figlet_format("Espiral Encripter", font = "slant" )
print(title)

option = 0
while option < 3:
    option = int(input("\nElija una opción => 1:Encriptar -  2:Desencriptar - 3:Finalizar :"))
    if option == 1:
        print('\nECRIPTADO')
        speed = int(input("Indique la frecuencia: "))
        encripter.spinner(speed)
        chars = input("Escriba su frase: ")
        encripter.encrypt(chars)
        option = 1

    if option == 2:
        print('\nDESENCRIPTADO')
        speed = int(input("Indique la frecuencia: "))
        encripter.spinner(speed)
        hash_encrypt = input("Ingrese su hash: ")
        encripter.decrypt(hash_encrypt)
        option = 2

    if option == 3:
        print('\n------ Fin del programa -------\n')    
        option = 3




