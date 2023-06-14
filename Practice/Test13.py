for num in range (100):
    print("Alvaro " + str(num))

#Tabla del 5
numero = 5
for x in range (0, 11):
        print(f" {numero} x {x} = {numero * x}")

#Tablas del 1 al 10
for a in range (1, 11):
    for b in range (1, 11):
        print(f"{a} x {b} = {a * b}")

#For para caracteres
texto = "Hola"
for t in texto:
    print(f"La palabra va en {t}")

#Ejemplo contador de caracteres
text = "Alvaro ramirez"
buscar = "r"
contador = 0
convertir = text.lower()
for c in convertir:
    if (buscar == c):
        contador += 1
print(f"El caracter {buscar} se repite {contador} veces")

#Valores de una lista
frutas=["Manzana", "Pera", "Naranja", "Sandia"]
x=0
for fru in frutas:
    x += 1 
    print(f"La fruta {x} es {fru}")
    
#Romper un bucle
lista = [1,2,3,4,5,6,7,8,9,10]
total=0
for x in lista:
    total += x
    if (x == 4):
        break
    print(f"El total es {total}")

#Continuar un bucle
for x in lista:
     total += x
     if (x == 5):
         continue
     print(f"El total es {total}")