# 11. Write a Python program to check if a string is a palindrome.
num = input("Enter any number: ")
reversed = num[::-1]
if(num == reversed):
    print(f"{num} is Palindrome number!")
else:
    print(f"{num} is not Palindrome number!")
