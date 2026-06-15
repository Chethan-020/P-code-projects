import math
def prime(num):
    is_prime=True
    if num==0:
        is_prime=False
    for i in range(2,math.ceil(num/2)+1):
        if num%i==0:
            is_prime=False
    if is_prime:
        print("Yes,It's a prime number")
    else:
        print("Not a prime number")

n=int(input("Enter the value:"))
prime(n)