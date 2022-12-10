# Set A -Strings
# 2) Write a python program to Reverse words in a given String

string = (input("Enter String :"))

words = string.split()

words = list(reversed(words))

print(" ".join(words))

# @Code By Rj

"""
Output:
Enter String :Hello Python 
python Hello
"""
