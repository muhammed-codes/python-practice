# Recursion is a func that calls itself

def add_one(num):
    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)

add_one(0)

# 
my_new_total = add_one(0)
print(my_new_total)

targets = 10
while targets <= 10:
    targets += 1
    print(targets)