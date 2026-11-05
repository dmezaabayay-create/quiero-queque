#archivo = open("uwu.txt", "w")
#archivo.write("Hola soy demian")
#archivo.write("\nWASAAAAAAAAAAA")
#archivo.close()

texto = open("uwu.txt","r")

for linea in texto:
    print(linea.strip())
    print(len(linea))
texto.close()

archivo = open("uwu.txt", "a")
archivo.write("\nkonichiwa")

archivo.close()