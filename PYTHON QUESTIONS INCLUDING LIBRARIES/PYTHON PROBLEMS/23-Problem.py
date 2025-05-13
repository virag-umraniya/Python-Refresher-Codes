# 23. Write a Python program to find the second largest element in a list.
lst = [10, 20, 5, 8, 30]
largest = max(lst)
lst.remove(largest)
sec_lar = max(lst)
print("Second largest element is:", sec_lar)