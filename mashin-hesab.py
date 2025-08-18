def addition (a, b):
    c = a + b
    print (c)

def subtraction (a, b):
    c = a - b
    print (c)

def multiplication (a, b):
    c = a * b
    print (c)

def divison (a, b):
    c = a / b
    print (c)

d = str(input("Choose your function?"))
while True:
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    if d == "addition":
        addition (a, b)
    elif d == "subtraction":
        subtraction (a, b)
    elif d == "multiplication":
        multiplication (a, b)
    elif d == "division":
        divison (a, b)
    else:
        print ("Error")
    