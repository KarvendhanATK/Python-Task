# Write a program that takes a string and
# returns True if it is an anagram of another string, False otherwise.

s1=input("Enter 1st string :")
s2=input("Enter 2nd string :")

print("1st input string :",s1)
print("2nd input string :",s2)
if len(s1)!=len(s2):
    print("Given string not anagram")
else:
    if sorted(s1)== sorted(s2):
        print("Given string is anagram")
    else:
        print("Given string not anagram")
