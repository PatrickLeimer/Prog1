#Lab 1 I/O Python
#Activity C
#Patrick Leimer 01/18/24

#gathers inputs
slope1 = float(input("Enter m for Line 1: "))
bComponent1 = float(input("Enter b for Line 1: "))
slope2 = float(input("Enter m for Line 2: "))
bComponent2 = float(input("Enter b for Line 2: "))
#calculates intersection coordinates
intersectionPointX = round((bComponent2 - bComponent1)/(slope1 - slope2), 2)
intersectionPointY = round((slope1*intersectionPointX + bComponent1), 2)
#prints coordinates
print(f"The intersection point is ({intersectionPointX}, {intersectionPointY})")