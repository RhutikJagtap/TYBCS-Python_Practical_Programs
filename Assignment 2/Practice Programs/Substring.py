# 2. Write a python program Check if a Substring is Present in a Given String

string = input("Enter string:")
sub_str = input("Enter word:")
if string.find(sub_str) == -1:
    print("Substring not found in string!")
else:
    print("Substring found in string!")

# @Code By Rj
"""
Output:
Enter string:Python is programming with Rj
Enter word:Rj
Substring found in string!

Enter string:python program
Enter word:programming
Substring not found in string!

"""
