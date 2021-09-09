

items = input("Enter any items seperated by space: ")

# Complete the program below

user_items = items.split()
for x in user_items:
    times = int(input(f"Repeat {x} how many times?: "))
    print((x + " ") *times)

print("Hello Kiddi")