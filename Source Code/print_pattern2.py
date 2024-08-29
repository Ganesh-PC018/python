def display_pattern(val):
    # Create the upper part of the diamond
    for i in range(val):
        spaces = '   ' * (val - i - 1)
        stars = ' * ' * (2 * i + 1)
        print(spaces + stars)

    # Create the lower part of the diamond
    for i in range(val - 2, -1, -1):
        spaces = '   ' * (val - i - 1)
        stars = ' * ' * (2 * i + 1)
        print(spaces + stars)

def print_pattern(num):
    if num < 1:
        return "Entered Value less than 1"
    else:
        display_pattern(num)

# Call the function and print the pattern
print(print_pattern(3))
