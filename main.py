easter_egg_number = 67

#function that adds 2 numbers
def add (x,y):
    if x + y == 67 or {x, y} == {2, 67}:
        print(("67 " * easter_egg_number).strip())
        return
    print(x+y)

#function that subtract 2 numbers
def subtract (x,y):
    print(x-y)

#function that multiplies 2 numbers
def multiply (x,y):
    print(x*y)

#function that divides 2 numbers 
def divide (x,y):
    print(x/y)

x = int(input("enter the first number:"))
y = int(input("enter the second number:"))

add(x,y)
print("welcome to Thomas's awesome calculator")
while True:
    print("what would you like to do?")
    print("type (a)dd (s)ubtract (m)ultiply (d)ivide (q)uit")

    user_choice=input(":")
    #print(user_choice)

    if user_choice == "a":
        add(x,y)
    elif user_choice == "s":
        subtract(x,y)
    elif user_choice == "m":
        multiply(x,y)           
    elif user_choice == "d":
        divide(x,y) 
    elif user_choice == "q":
        print("goodbye")
        break