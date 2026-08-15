value = 1
while value <= 10:
    print(value)
    if value == 5:
        break
    value += 1

while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)

names = ["Ahmad", "Ali", "Omar", "Sara", "Lina", "Mona"]

for name in names:
    print(name)

for x in range(5):
    print(x, "- this is Ahmad")
    for y in range(3):
        print(y, "- this is Ali")

for i in range(20, 40, 3): # start - end - step
    print(i)
else:
    print("Done")

names = ["Ahmad", "Ali", "Omar", "Sara", "Lina", "Mona"]
actions = ["Eats", "Sleeps", "Codes", "Drinks", "Thinks", "Talks", "Walks", "Runs"]

for name in names:
    for action in actions:
        print(name, " ", action)