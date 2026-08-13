users = ["Alice", "Bob", "Charlie"]

data = ["Alice", 39, True]

emptylist = []

print("Bob" in users)  # True
print("David" in users)  # False

print(data[1])

print(data.index("Alice"))  # 0
# print(data.index(40))  # Throws error because 40 is not in the list

users.append('Muhammed')
users += ['Ibrahim', 'Ayub']
users.extend(['Aisha', 'Ruqoyyah'])

users.extend(data)

# adding values to a specific index
users.insert(0, "Sulayman")

users.remove("Ayub")
users.pop(0)  # Removes the first item in the list, if nth in the bracket means remove last item

del users[0]  # Removes the first item in the list

# del data # deletes the list entirely

emptylist.clear()  # Clears the list but keeps it in memory

newList = ["apple", "banana", "cherry", "Date", "GRAPES"]

#sortings
newList.sort(key=str.lower)  # Sorts the list in ascending order
newList.sort(reverse=True)  # Sorts the list in descending order
newList.sort(key=len)  # Sorts the list based on the length of the items in ascending order
newList.sort(key=str.lower, reverse=True)  # Sorts the list based on the length of the items in descending order and ignores case sensitivity
print(newList)


numbers = [5, 2, 9, 1, 7]
numbers.sort()  # Sorts the list in ascending order
numbers.reverse()  # Reverses the order of the list