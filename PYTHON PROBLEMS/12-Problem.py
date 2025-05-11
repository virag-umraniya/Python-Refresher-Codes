# 12. Write a Python program to count the number of vowels in a string.
str = "Hello, My name is frank Abagnale Jr."
vowels = 0
for i in str:
    if i.lower() in 'aeiou':
        vowels += 1
print("Number of vowels are:",vowels)