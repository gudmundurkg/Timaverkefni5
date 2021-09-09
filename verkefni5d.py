a_str = input("Enter a string: ")

# Complete the program below

for letter in (a_str):
    if letter == letter.upper():
        letter = letter.lower()
    elif letter == letter.lower():
        letter = letter.upper()
    print(letter, end='')

