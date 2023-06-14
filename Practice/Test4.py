#Ejercicio 4
name = input("Ingrese su nombre: ")
workedHours = input("Ingrese la cantidad de horas trabajadas: ")
costPerHour = input("Ingrese el coste por hora: ")

total = float(workedHours) * float(costPerHour)

print("El total a pagar por " + name + " es: " + str(total))