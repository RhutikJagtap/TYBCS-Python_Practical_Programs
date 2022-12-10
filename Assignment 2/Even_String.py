# Set B-Strings
# 1. Write a python program to print even length words in a string.
def printWords(s):

    string = s.split(' ')

    for word in string:

        # if length is even
        if len(word) % 2 == 0:
            print(word)


# Driver Code
string = input("Enter the String :")
printWords(string)

# Code By Rj
"""
Output:
Enter the String :hello python programming with rj
python
with
rj
"""
