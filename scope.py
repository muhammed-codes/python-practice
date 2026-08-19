name = "Muhammed" # global scope - can be used anywhere
count = 2

def greeting(firstName):
    color = "blue" # local scope, can only be used in this func
    print(f"{firstName}'s favourite color is {color}.")

greeting(name)

print(count)

# defining a func inside another func
def another_func():
    global count
    count += 2
    color = "red"
    def greeting(firstName): # nested func
        print(f"{firstName}'s favourite color is {color} and number is {count}.")
    greeting("Fawaz")

another_func()