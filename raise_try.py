def divide( a, b):
    if type(a) !=int or  type(b) !=int :
        raise ValueError("Not valid type given!!")
    
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    

    return a / b

try :
    print(divide(10, 2))


except ValueError as e:
    print(f"ValueError: {e}")