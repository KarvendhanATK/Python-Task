#) Write a program that takes a string and
# returns a new string with all the vowels removed.

str=input("Enter input string:")
vowel_string="aeiouAEIOU"
print("Input string: ",str)

for char in str:
    if char in vowel_string:
        str=str.replace(char,"")


print("Output string without vowels:",str)








