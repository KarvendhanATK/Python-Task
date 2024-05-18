# Create a Pyramid of Numbers from 1 to 20 using For loop

max_number=20

for i in range(1,max_number+1):
    space=max_number-i
    print(" " * space,end="")


    for j in range(1,i+1):
        print(j, end=" ")

    print()

