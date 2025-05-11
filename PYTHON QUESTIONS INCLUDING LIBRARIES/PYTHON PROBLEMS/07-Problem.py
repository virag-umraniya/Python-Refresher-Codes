# 7. Write a Python program to check if a number is prime.
a = 17
is_prime = True
if(a<1):
    print(f"The number {a} is not Prime!")
else:
    for i in range(2, a):
        if(a %i == 0):
            is_prime = False
            break
        
    if(is_prime):
        print(f"The number {a} is Prime!")
    else:
        print(f"The number {a} is not Prime!")

