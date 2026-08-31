def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    elif n < 1:
        return "Argument must be an integer greater than 0."
    else:
        final_num = ""
        for i in range(1, n + 1):
            final_num += str(i)
            if i < n:
                final_num += " "
        return final_num

new = number_pattern(6)
print(new)