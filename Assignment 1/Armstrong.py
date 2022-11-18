# 4.Write python program to check Armstrong Number
n = int(input("Enter Number:"))
temp = n
sum = 0
while (n > 0):
    rem = n % 10
    sum = sum + (rem * rem * rem)
    n = n //10  #floor division
if (temp== sum):
    print(temp, "is an armstrong")
else:
    print(temp, "is not an armstrong")

# Code By Rj