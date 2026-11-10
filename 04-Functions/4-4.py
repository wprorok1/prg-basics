###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    abs_number = abs(number)
    number2 = str(abs_number)
    total_sum = 0
    for digit_char in number2 :
        total_sum += int(digit_char)
    return total_sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')