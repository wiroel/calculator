

def calc(choice, a, b):
    if choice == '+':
        add = a + b
        return(add)
    elif choice == '-':
        sub = a - b
        return(sub)
    elif choice == '*':
        mul = a*b
        return(mul)
    elif choice == '/':
        try:
            div = a/b
            return(div)
        except ZeroDivisionError:           
            return("Not divisible")
            
valid_sign = ['+', '-', '*', '/']

try:
    user_input = input("""
                   choices:
                   +. for addition
                   -. for subtraction
                   *. for multiplication
                   /. for division
                   Enter your choice: """)
    if user_input not in valid_sign:
        raise ValueError("Invalid sign")            #"raise" allows to put some string into the value error,, ettikai valueerror use garda,, we cant input the string
    a = int(input("Enter 1st num:"))
    b = int(input("Enter 2nd num:"))


    result = (calc(choice = user_input, a=a, b=b))       #maathi return garey paxi muni function print is a must

    print(f"{a} {user_input} {b} = {result}")
except ValueError as c:
    print(c)