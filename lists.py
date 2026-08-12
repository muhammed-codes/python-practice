users = ["Alice", "Bob", "Charlie"]

data = ["Alice", 39, True]

emptylist = []

print("Bob" in users)  # True
print("David" in users)  # False

print(data[1])

print(data.index("Alice"))  # 0
print(data.index(40))  # Throws error because 40 is not in the list
