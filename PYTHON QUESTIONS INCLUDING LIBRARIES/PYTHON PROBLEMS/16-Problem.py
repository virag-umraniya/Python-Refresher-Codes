# 16. Write a Python program to find the least common multiple (LCM) of two numbers.
def find_gcd(a, b):
    while b:
        a,b = b, a%b # Concept of tuple Unpacking
    return a

def find_lcm(a,b):
    gcd = find_gcd(a,b)
    lcm = (a * b) // gcd
    return lcm
a = 2
b = 3
print("LCM is:",find_lcm(a,b))