## podemos utilizar esta forma de almacenar los caracteres para encriptar un mensaje de forma sencilla con una encriptacion por deplazamiento
## tambien conocida como cifrado cesar
# print(ord(letra))   #codigo ASCII
# print(chr(43))      #convierte de codigo a caracter

# Cifrado
cadena=input("$>")
cadenaCodificada=""
desplazamiento=7
for letra in cadena:
    cadenaCodificada = cadenaCodificada+chr(ord(letra)+desplazamiento)

print(cadena)
print(cadenaCodificada)