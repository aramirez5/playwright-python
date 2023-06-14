#Ejemplo1
# flag=True
# count=0
# while (flag == True):
#     print(f"Hello World {count}")
#     count=count+1
#     if count == 5:
#         flag=False

#Ejemplo2
# num=0
# while num!=3:
#     a=0
#     b=0
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Exit")
#     num=int(input("Enter a number: "))  
#     if num==1 or num==2 or num==3:
#         if num==1:
#             a=float(input("Give me first number: "))
#             b=float(input("Give me second number: "))
#             sum=a+b
#             print(f"The sum is {sum}")
#         elif num==2:
#             a=float(input("Give me first number: "))
#             b=float(input("Give me second number: "))
#             sum=a-b
#             print(f"The sub is {sum}")
#         else:
#             print("Bye, thank you")
#     else:
#         print("Select an option betweeen 1-3 \n\n")

#Ejemplo3
number=1
bandera=True

# while bandera==True:
#     a=0
#     b=0
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Exit")
#     num=int(input("Enter a number: "))  
#     if num==1 or num==2 or num==3:
#         if num==1:
#             a=float(input("Give me first number: "))
#             b=float(input("Give me second number: "))
#             sum=a+b
#             print(f"The sum is {sum}")
#         elif num==2:
#             a=float(input("Give me first number: "))
#             b=float(input("Give me second number: "))
#             sum=a-b
#             print(f"The sub is {sum}")
#         else:
#             print("Bye, thank you")
#             bandera=False
#     else:
#         print("Select an option betweeen 1-3 \n\n")

#Ejemplo4
import random

num=random.randint(1,20)
bandera=True

while bandera==True:
    n=int(input("Enter a number between 1 and 20: "))
    if n>0 and n<=20:
        if n == num:
            print("You guessed it!")
            bandera=False
        elif n < num:
            print("Too low")
        elif n > num:
            print("Too high")
    else:
        print("Please, you must enter a number between 1 and 20")