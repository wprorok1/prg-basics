###
# Calculation of circle area and circumference 
import math
# determine radius and PI values
radius = int(input("Enter radius: "))
# calculate area
area = math.pi * radius**2
# calculate circumference 
circumference = 2 * radius * math.pi
# print results
print(f'Circle area: {area}')
print(f'Circle circumference: {circumference}')

