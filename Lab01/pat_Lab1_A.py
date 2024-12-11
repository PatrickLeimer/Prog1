
#Lab 1 I/O Python
#Activity A
#Patrick Leimer 01/18/24

#gathers resistance values
res_01 = float(input("What is the value of R1? "))
res_02 = float(input("What is the value of R2? "))
res_03 = float(input("What is the value of R3? "))

final_Resistance = round(1 / ((1/res_01) + (1/res_02) + (1/res_03)), 2)
#calculates final R, and rounds to two decimal places, then print
print("The equivalent resistance is", final_Resistance, "ohms")

