#  Write a Python program to calculate the total number of Vowels
# and Count of each individual vowel A,E,I,O,U
# in the string "Guvi Geeks Network Private Limited"?

#Total count of Vowels
t="Guvi Geeks Network Private Limited"
c=0
for i in t:
    if i in "aeiouAEIOU":
        c=c+1
print("The Total Number Of Vowels count =",c)

# Vowels individual Count
#Total A count
a=0
for i in t:
    if i in "Aa":
        a=a+1
print("Vowel A Count =",a)

# total E count
e=0
for i in t:
    if i in "eE":
        e=e+1
print("Vowel E Count =",e)

#Total I count
j=0
for i in t:
    if i in "Ii":
        j=j+1
print("Vowel I Count =",j)

#Total O count
o=0
for i in t:
    if i in "oO":
        o=o+1
print("Vowel O Count =",o)


#total U count
u=0
for i in t:
    if i in "Uu":
        u=u+1
print("Vowel U Count =",u)