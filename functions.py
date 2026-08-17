def my_name():
    print("My name is Muhammed")

my_name()

def sum(num1 = 0, num2 = 0):
    if (type(num1) is not int or type(num2) is not int):
        return
    return(num1 + num2)

sum(3, 7)

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Muhamed", "Ahmad", "Ruquyah")