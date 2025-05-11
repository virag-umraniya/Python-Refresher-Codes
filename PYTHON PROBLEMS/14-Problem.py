# 14. Write a Python program to find the sum of digits in a number.
a = 1234
sum = 0
while(a > 0):
    digit = a % 10
    sum += digit
    a = a // 10
print("sum of digits in a number is:",sum)