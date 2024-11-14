print("-Calculator Project-")

# Function
def addition(n1, n2):
    return n1 + n2
def subtraction(n1, n2):
    return n1 - n2
def multiplication(n1, n2):
    return n1 * n2
def division(n1, n2):
    return n1 / n2

while True:
    print("01. Addition(+)")
    print("02. Subtraction(-)")
    print("03. Multiplication(*)")
    print("04. Division(/)")
    option = int (input("Select operations form 1, 2, 3, 4 : "))

    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    
    if option in [1, 2, 3, 4]:
        if option == 1:
            print (n1, "+", n2, "=", addition(n1, n2))
        elif option == 2:
            print (n1, "-", n2, "=", subtraction(n1, n2))
        elif option == 3:
            print (n1, "*", n2, "=", multiplication(n1, n2))
        elif option == 4:
            print (n1, "/", n2, "=", division(n1, n2))
    else : 
        print("Invalid Input")