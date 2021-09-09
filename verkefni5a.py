a_str = input("Input a string: ")
char_to_count = input("Input a character to count: ")

# Complete the program below

index = 0
while index < len(a_str):
    index = a_str.find(char_to_count, index)
    if index == -1:
            break
    print(index)
    index += 1

