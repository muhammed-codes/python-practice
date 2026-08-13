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
print(newList)
newList.sort(reverse=True)  # Sorts the list in descending order
print(newList)
newList.sort(key=len)  # Sorts the list based on the length of the items in ascending order
print(newList)
newList.sort(key=str.lower, reverse=True)  # Sorts the list based on the length of the items in descending order and ignores case sensitivity
print(newList)


numbers = [5, 2, 9, 1, 7]
numbers.sort()  # Sorts the list in ascending order
print(numbers)
numbers.reverse()  # Reverses the order of the list

# lists are mutable and tuples are immutable (can not be modified, sorted etc)
mytuples = ("apple", "banana", "cherry")
print(mytuples) 
newtuple = ("apple", "banana", "cherry")  # tuple literal
print(newtuple)

#getting creative by converting a tuple to a list and back to a tuple
names = ("Alice", "Bob", "Charlie")
names_list = list(names)  # Convert tuple to list
names_list.append("David")  # Modify the list
names = tuple(names_list)  # Convert list back to tuple

# unpacking tuples
person = ("Alice", 30, "Engineer", "Content Creator")
name, age, *profession = person  # Unpacking the tuple into variables
print(name)  # Output: Alice
print(age)  # Output: 30
print(profession)  # Output: Engineer, Content Creator

# dot notations
# once u typed any variable name and a dot, it will show you all the methods available for that variable type. For example, if you type "users." it will show you all the methods available for lists.