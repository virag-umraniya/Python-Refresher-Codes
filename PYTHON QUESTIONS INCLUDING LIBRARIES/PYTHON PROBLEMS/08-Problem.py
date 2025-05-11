# 8. Write a Python program to print the multiplication table of a number.
a = int(input("Enter any number to get its multiplication table: "))
for i in range(1,11):
    print(f"{a} x {i} =", a * i)