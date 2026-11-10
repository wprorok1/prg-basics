###
# Program for testing built-in functions
 #   Using built-in Python functions, write a program that calculates and prints:

#the largest number: 7,5,6,3,8,2
#the smallest number: 4,7,2,3,9,8
#length of the phrase: "computer science"
#letter read from the keyboard
#number representing the string "20303"
#binary string representing decimal number 304
#hexadecimal string representing decimal number 304
#integer representing the Unicode code of the € sign
#absolute value of -17
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

letter_read = input('Type a letter: ')
print('Letter read:', letter_read)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

num_rep = int('20303')
print('Number representation of 20303 is ', num_rep)

binary = bin(304)
print('The binary string of 304 is ', binary)

hexadecimal = hex(304)
print('The hexadecimal string of 304 is ', hexadecimal)

int_uni = ord('€')
print('The integer representing € is', int_uni)

absolute = abs(-17)
print('The absolute value of -17 is', absolute)




