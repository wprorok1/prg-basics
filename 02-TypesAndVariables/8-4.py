###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170
feet = int(cm / 2.54 // 12)
inches = int((cm / 2.54) % 12)
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')