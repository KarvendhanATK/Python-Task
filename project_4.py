
#Write a program that takes a string and
# returns the number of unique characters in it.


s=input("Enter New String :")
print("Input String:",s)

d={}

for i in s:
    d[i]=0
print(d)
for i in s:
    d[i]=d[i]+1
print(d)