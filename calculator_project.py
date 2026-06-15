import random
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operation_symbols={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def new_calculation():
    num1=float(random.randrange(1,100))
    print(f"Enter the value of num1:{num1}")
    for symbol in operation_symbols:
        print(symbol)
    continue_flag=False
    while not continue_flag:
        operation=input("Enter an operator:")
        num2=float(random.randrange(1,100))
        print(f"Enter the value of num2:{num2}")
        calculation=operation_symbols[operation]
        output=calculation(num1,num2)
        print(f"{num1} {operation} {num2} = {output}")
        repeat=input(f"Enter 'y' to continue calculation with {output} or 'n' to start new calculation or press any key  to exit:").lower()
        if repeat=="y":
            num1=output
            continue_flag=False
        elif repeat=="n":
            continue_flag=True
            new_calculation()
        else :
            continue_flag=True
            print("End of the program.")
new_calculation()
            
        