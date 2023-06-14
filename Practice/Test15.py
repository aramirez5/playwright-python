#Función con argumentos
def saludar(nombre):
    print("Hola", nombre)

saludar("Juan")

#Sumar dos números
def sumar():
    a=int(input("Ingrese el primer número: "))
    b=int(input("Ingrese el segundo número: "))
    if a > 0 and b > 0:
        suma=a+b
        res=a-b
        mul=a*b
        return suma, res, mul
    else:
        print("Los números deben ser positivos")

# resultado=sumar()
# print(f"La suma es: {resultado}")

# rs, rr, rm=sumar()

# print(f"La suma es: {rs}")
# print(f"La resta es: {rr}")
# print(f"La multiplicación es: {rm}")

# total=rs+rr+rm
# print(f"El total es: {total}")

#Otro ejemplo
def giveTwo():
    v1=int(input("Ingrese el primer número: "))
    v2=int(input("Ingrese el segundo número: ")) 
    return v1, v2

def sumTwo(a,b):
    suma=a+b
    return suma

x1,x2=giveTwo()
result=sumTwo(x1,x2)
print(f"La suma es: {result}")