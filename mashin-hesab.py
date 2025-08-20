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

def exponent (a, b):
    c = a ** b
    print (c)


while True:
    print ("Calculator")
    print ("1. Addition    (+)")
    print ("2. Subtraction (-)")
    print ("3. Multiply    (*)")
    print ("4. Division    (/)")
    print ("5. Exponent    (^)")
    d = float (input("Which one? "))
    a = float (input("Enter First Number: "))
    b = float (input("Enter Second Number: "))
    
    if d == 1:
        addition (a, b)
    elif d == 2:
        subtraction (a, b)
    elif d == 3:
        multiplication (a, b)
    elif d == 4:
        divison (a, b)
    elif d == 5:
        exponent (a, b)
    else:
        print ("Error!")
    
    
    