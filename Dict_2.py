a = {"key" : "value",
     "Name" : "Hiten",
     "friends" : ["Alice", "Bob", "Charlie"],
     "age" : 21,
     "Marks" : [98,99,100]
    }

print(a.items())
print(a.keys())
print(a.values())
print(a.get("Name"))
print(a.get("friends"))
print(a.get("age"))
print(a.get("Marks"))
print(a.get("nonexistent_key", "Default Value"))  # Returns "Default Value" if key doesn't exist

print(a.pop("age"))  # Removes and returns the value associated with the key "age"

#print(a["age"]) # This will raise a KeyError since "age" has been removed from the dictionary

print(a.popitem())  # Removes and returns the last inserted key-value pair as a tuple
print(a)
print(a.copy())  # Returns a shallow copy of the dictionary