#PROGRAM TO CREATE A BASIC CALCULATOR

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print("Please select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

choice = int(input("Select operation (1-4): "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == 1:
    print(a, "+", b, "=", add(a,b))
elif choice== 2:
    print(a, "-", b, "=", sub(a,b))
elif choice == 3:
    print(b, "*", b, "=", mul(a,b))
elif choice== 4:
    print(a, "/", b, "=", div(a,b))
else:
    print("Invalid input")

