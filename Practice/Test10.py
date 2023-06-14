a = 20
b = 30

if a > b:
    print("a is greater than b")
    print(str(a) + " > " + str(b))

elif a < b:
    print("b is greater than a")
    print(str(b) + " > " + str(a))

elif a == b:
    print("a is equal to b")
    print(str(a) + " = " + str(b))

elif a != b:
    print("a is different to b")
    print(str(a) + " != " + str(b))

else:
    print("Something went wrong")