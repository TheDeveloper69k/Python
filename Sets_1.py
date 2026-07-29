s = set()

s = {1, 2, 7 , 6 ,2 ,2} #Duplicate values will be removed automatically

print(s, type(s))

print(len(s))  # Output: 4

s.remove(2)  # Removes the element 2 from the set
print(s)  # Output: {1, 6, 7}

s.pop()  # Removes and returns an arbitrary element from the set
print(s)  # Output: {6, 7} (the order may vary)

s.clear()  # Removes all elements from the set
print(s)  # Output: set() (an empty set)

