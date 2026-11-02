###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print(str.upper(movie))

# print title in small letters
print(str.lower(movie))

# print how many times the vowel "e" appears in the title
print(str.count(movie, 'e'))

# print where in the text is the word "Lord"
print(str.find(movie, 'Lord'))

# print where in the text is the word "dragon"
print(str.find(movie, 'dragon'))