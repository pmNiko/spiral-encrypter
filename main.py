from encrypter import Encrypter

print("Spiral Encrypter")

encripter = Encrypter()

speed = int(input("Indique frecuencia: "))
encripter.spinner(speed)

chars = input("Escriba su frase: ")
encripter.encrypt(chars)

hash_encrypt = input("\nDesencripte su hash: ")
encripter.decrypt(hash_encrypt)




