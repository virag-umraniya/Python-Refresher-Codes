# 15. Write a Python program to find the greatest common divisor (GCD) of two numbers.
def find_gcd(a, b):
    while b:
        a,b = b, a%b # Concept of tuple Unpacking
    return a
a = 12
b = 34

print("GCD is:",find_gcd(a,b))