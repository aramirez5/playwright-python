#First
frutas = tuple(['manzana', 'banana', 'naranja', 'pera'])
print(frutas)
print(frutas[0])
print(frutas[1])
print(len(frutas))
print(type(frutas))

#Second
frutas = tuple(['manzana', 'banana', 'naranja', 'pera'])
tupla2 = (1, 2, 3, 4, 5)
tupla3 = (True, False, True)
tupla4 = (1, 2, 3, "Rodrigo", "Juan", [4, 5, 6], True)
print(frutas)
print(tupla2)
print(tupla3)
print(tupla4)
print(tupla4[5][2])

#Third
tupla1 = ('manzana', 'banana', 'naranja', 'pera')
tupla2 = (1, 2, 3, 4, 5, 6, 2, 3, 3, 1, 7, 3)
tup2, tup3, tup4, tup5 = tupla1
print(tup2)
print(tup3)
print(tup4)
print(tup5)
tupla_lista=list(tupla1)
print(tupla_lista)

print('manzana' in tupla1)
print(tupla2.count(3))
if tupla2.count(3) > 2:
    print(f"Hay mas de dos veces el numero 3, existen {tupla2.count(3)}")