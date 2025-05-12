# 21. Write a Python program to check if a year is a leap year.
year = 2023
if(year %4 == 0 or year %100 != 0 and year %400 == 0):
    print(f"The {year} year is a leap year: ")
else:
    print(f"The {year} year is not a leap year: ")