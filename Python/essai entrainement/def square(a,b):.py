def square(height,width):
    for i in range(height):
        for j in range(width):
            print("*", end="")  
        print()

i = int(input("height = "))
j = int(input("width = "))
square(i,j)
#range = ça prend un argument qui est 
# un chiffre dans ce cas là i va jusqu'à range
#help(range)