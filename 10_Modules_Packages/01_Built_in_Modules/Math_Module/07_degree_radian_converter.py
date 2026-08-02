import math
degree = float(input("Enter degree: "))
radian = float(input("Enter radian: "))
converted_degree = math.radians(degree)
converted_radian = math.degrees(radian)
print(f"{degree} degrees = {converted_degree} radians")
print(f"{radian} radians = {converted_radian} degrees")