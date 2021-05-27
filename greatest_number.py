print("Starting Program")

A = int(input("Enter the first number\n"))
B = int(input("Enter the second number\n"))
C = int(input("Enter the third number\n"))

if (A>B):
    if(A>C):
        print(A,"is the greatest number")
    else:
        print(C,"is the greatest number")
else:
    if (B>C):
        print(B, "is the greatest number")
    else:
        print(C, "is the greatest number")

print("Ending Program...")