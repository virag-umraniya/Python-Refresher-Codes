# 9. Write a Python program to find the factorial of a number.
a = 0
factorial = 1
if(a<0):
    print("factorial does not exist for negative numbers!")
elif(a == 0):
    print("Factorial of 0 is 1")
else:
    for i in range(1,a+1):
        factorial *= i
    print("Factorial is:", factorial)