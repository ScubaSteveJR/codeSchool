import math

weight = float(input("What is the weight? "))
height = float(input("What is the height? "))
weightkg = float(weight / 2.2)
heightcm = float(height * 2.54)
bsa = math.sqrt(((weightkg * heightcm) / 3600))

print(f"BSA: {bsa}")