def display_pattern(num):
    if num < 1:
        return "Enter number greater than 1"
    
    if num != int(num) or num < 1:
        return "Enter a positive integer value"
    
    num = int(num)
    col = ((num + 1) * 2) + 1
    row = ((num + 1) * 2) - 1

    # Top part of the pattern
    for i in range((row // 2) + 1):
        for j in range(col):
            if (j + i) == col // 2 or (j - i) == col // 2:
                print(" *", end="")
            elif j == (row // 2) + 1 and i == (j - 1):
                print("",num, end="")
            else:
                print("  ", end="")
        print()

    # Middle part of the pattern
    for i in range((row // 2) - 1, 0, -1):
        for j in range(col):
            if (j + i) == col // 2 or (j - i) == col // 2:
                print(" *", end="")
            else:
                print("  ", end="")
        print()

    # Bottom part of the pattern
    for _ in range(num):
        print(" *" * col)

def print_pattern(num):
    result = display_pattern(num)
    if result:
        print(result)

# Test with a range of numbers
for i in range(10,13): 
    print_pattern(i)
