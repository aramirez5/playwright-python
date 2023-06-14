#Capitalize
name1 = "demo de la aplicación"
name1 = name1.capitalize()
print("Ejemplo de capitalize: " + name1)

#Casefold
name2 = "Demo de la aplicación"
name2 = name2.casefold()
print("Ejemplo de casefold: " + name2)

#Center
name3 = "Demo de la aplicación"
name3 = name3.center(50)
print("Ejemplo de center: " + name3)

#Count
name4 = "Demo de la aplicación"
name4 = name4.count("Demo")
print("Ejemplo de count: " + str(name4))

#EndWith
name5 = "Demo de la aplicación"
name5 = name5.endswith("aplicación")
print("Ejemplo de endswith: " + str(name5))

#Find
name6 = "Demo de la aplicación"
name6 = name6.find("aplicación")
print("Ejemplo de find: " + str(name6))

#Corte de cadenas
name7 = "Demo de la aplicación"
print(name7[1:12])
print(name7[:5])
print(name7[5:])

#Cadena a mayúsculas
name8 = "Demo de la aplicación"
name8 = name8.upper()
print(name8)

#Cadena a minúsculas
name9 = "Demo de la aplicación"
name9 = name9.lower()
print(name9)

#Eliminar espacios
name10 = "      Demo de la aplicación      "
name10 = name10.strip()
print(name10)

#Sustituir palabra
name11 = "Demo de la aplicación"
name11 = name11.replace("aplicación","programación")
print(name11)

#Escape
name12 = "Demo de la \"aplicación\""
name12 = name12.replace("aplicación","programación")
print(name12)
name13 = "\tEsto tiene un espacio al inicio tab\n\t\tEsto es otra línea\n\t\t\t\rEsta es la tercera línea, pero sin tab"
print(name13)