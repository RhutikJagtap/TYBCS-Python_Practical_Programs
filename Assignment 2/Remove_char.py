#Set A-Strings
# 3) Write a python program to remove i’th character from string in different ways
String = input("Enter the string : ")
i = int(input("Enter the index of character to be removed : "))

resetString = ""

for index in range(len(String)):
    if index != i:
        resetString = resetString + String[index]

print("Entered string : " + String)
print("String formed by removing i'th character : " + resetString)

# @Code By Rj
"""
Output:
Enter the string : Hello python
Enter the index of character to be removed : 1
Entered String: Hello python
String formed by removing i'th character :  Hllo Python
"""
