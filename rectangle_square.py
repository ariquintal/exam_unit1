print("Start Program")

width = int(input("Insert the width\n"))
lenght = int(input("Insert the lenght\n"))

area = width * lenght

if lenght == width:
    print("This a square with an area of", area)
else:
    print("This is a rectangle with an area of", area)

print("Ending Program...")