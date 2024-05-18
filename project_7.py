# Write a program that takes a string and
# returns the most frequent character in it.

s=input("Enter a string: ")

print("Given string:",s)
freq={}

for i in s:
    if i in freq:
        freq [i]+=1
    else:
        freq [i]=1
result=max(freq,key=freq.get)

print("The most frequent word is ", result)