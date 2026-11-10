###
# Sums numbers entered by user
#
total_sum = 0
count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    count += 1
    arithm_mean = total_sum / count 

print(f"The arithmetic mean of the numbers is: {arithm_mean}")