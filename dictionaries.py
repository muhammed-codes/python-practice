# DICTIONARIES - like JS objects
band = {
"vocals": "Plant",
"guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")
print(f"{band} okay {band2}")
print(type(band))

# accessing dicts
print(band["guitar"]) # the guitar is the key
print(band2.get("vocals")) # the vocals is the key

# list all keys
print(band.keys())

#list all values
print(band.values())

# list all keys/values as tuples
print(band.items())

# verify a key exists in a dict
print("vocals" in band) # True
print("bass" in band) # False

# changing values in a dict
band["guitar"] = "Pagey"
band2.update({"guitar": "Pagey"})

# removing items from a dict
del band["vocals"] 
print(band.pop("guitar")) # removes the key and returns the value

# adding items to a dict
band["bass"] = "Jones"

# delete and clear a dict
band.clear() # removes all items from the dict

# copying a dict
band3 = band2.copy() # creates a shallow copy of the dict

# nested dicts
band4 = {
    "vocals": "Plant",
    "guitar": "Page",
    "members": {
        "drums": "Bonham",
        "bass": "Jones"
    }
}

# accessing nested dicts
print(band4["members"]["drums"]) # Bonham

# sets - no duplicates allowed in sets
numberss = {1, 2, 3, 4, 5}
numberss.add(6) # add an item to the set
numberss.remove(3) # remove an item from the set

# add elements from another set
more_numbers = {7, 8, 9}
numberss.update(more_numbers) # add multiple items to the set

# merge 2 sets to create a new set
merged_set = numberss.union(more_numbers) # creates a new set with all unique items