def base_num(val, base, base2):
    # Convert the input number from the original base to decimal
    decimal_ans = 0
    k = 0
    while val > 0:
        rem = val % 10
        decimal_ans += rem * (base ** k)
        val = val // 10
        k += 1
    
    # Convert the decimal number to the target base
    if decimal_ans == 0:
        return "0"
    
    ans = ""
    while decimal_ans > 0:
        rem = decimal_ans % base2
        decimal_ans = decimal_ans // base2
        ans = str(rem) + ans
    
    return ans

print("Ans : ", base_num(100000, 8, 16))  
print("Ans : ", base_num(10, 2, 10))      
