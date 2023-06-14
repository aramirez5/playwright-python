list = [1,2,3,4,5,6,7,8,9,10]
print(list)
print(list[0])
print(list[0:2])

#Longitud
print(len(list))

#Añadir valor al final
list.append(11)
print(list)

#Añadir con insert
list.insert(4,5)
print(list)

#Sumando varias listas
list2 = [12,13,14,15,16,17,18,19,20]
list3 = list + list2
print(list3)

#Buscar un elemento
print(13 in list2)

#Saber donde está cada elemento
print(list2.index(13))

#Contar el número de elementos
print(list2.count(13))

#Eliminar el último elemento
list2.pop()
print(list2)

#Eliminar con remove
list2.remove(13)
print(list2)

#Limpiar la lista
list2.clear()
print(list2)

#Invertir el orden de la lista
list2 = [12,13,14,15,16,17,18,19,20]
list2.reverse()
print(list2)

#Ordenar la lista
list2.sort()
print(list2)