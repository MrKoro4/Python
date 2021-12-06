from math import sqrt

def discriminant(a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print("no solutions") 
    elif delta == 0:
        x0 = -b/(a*2)
        print("x0 = ", x0)
    else:
        x1 = (-b-(sqrt(delta)))/(a*2)    
        print("x1 = ", x1)
        x2 = (-b+(sqrt(delta)))/(a*2)
        print("x2 = ", x2)

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
discriminant(a, b, c)
