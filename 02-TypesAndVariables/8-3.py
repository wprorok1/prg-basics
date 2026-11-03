###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# determine celsius temperature value
# make calculations to convert C to F and K
# print results

Celsius = int(input('Enter temperature in Celsius: '))
Farenheit = Celsius * 1.8 + 32
Kelvin = Celsius + 273.15

print(f'Celsius temperature: {Celsius}')
print(f'Fahrenheit temperature: {Farenheit}')
print(f'Kelvin temperature: {Kelvin}')