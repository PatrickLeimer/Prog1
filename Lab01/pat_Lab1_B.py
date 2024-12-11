#Lab 1 I/O Python
#Activity B
#Patrick Leimer 01/18/24
import math
#Gathers length and width and calculates data
length1 = float(input("Enter the length: "))
width1 = float(input("Enter the width: "))
perimeter1 = round(2*length1 + 2*width1, 2)
area1 = round(width1 * length1, 2)
diagonal1 = round(math.sqrt(width1**2 + length1**2), 2)
#prints calculated data
print("Rectangle perimeter:", perimeter1)
print("Rectangle area:", area1)
print("Rectangle diagonal:", diagonal1)