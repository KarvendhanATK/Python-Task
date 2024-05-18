# Write a program that takes two strings and
# returns the longest common substring between them.

s1=input("input 1 st string:")
s2=input("input 2nd string: ")
print(" Input 1st string:")
print("Input 2nd string: ")

a=s1.split()
b=s2.split()
for i in a:
    if i in b:
        print("Two common substring:",i)