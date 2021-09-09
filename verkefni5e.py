a_str = input("Enter a string: ")

# Complete the program below
back_a_str = a_str[::-1]

if a_str == back_a_str:
    print("Palindrome!")
else:
    print("Nothing special about this string :(")