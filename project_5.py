#Write a program that takes a string and returns True if it is a palindrome,
# False otherwise.

s=input("enter word: ")
s=s.lower()
print("enter word : ",s)

def palindrome(s):
    s==s[::-1]

ans=palindrome(s)

if ans:
    print(s,"is a palindrome","(true)")
else:
    print(s,"is not a palindrome", "(False)")