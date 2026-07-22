a = ["Hiten" , 69 , 3.14 , True]

#INDEXING
print(a[0])  # Output: Hiten
print(a[1])  # Output: 69
print(a[2])  # Output: 3.14
print(a[3])  # Output: True

#NEGATIVE INDEXING
print(a[-1])  # Output: True (last element)
print(a[-2])  # Output: 3.14 (second last element)
print(a[-3])  # Output: 69 (third last element)
print(a[-4])  # Output: Hiten (fourth last element)

#SLICING
print(a[1:3])  # Output: [69, 3.14]
print(a[:2])  # Output: ['Hiten', 69]
print(a[2:4])  # Output: [3.14, True]

#MODIFYING LISTS
print(a.append("Apple"))  # Adds "Apple" to the end of the list
print(a.reverse())  # Reverses the list
print(a.remove(69))  # Removes the first occurrence of 69 from the list
print(a.pop())  # Removes and returns the last item from the list
print(a.insert(1, "Banana"))  # Inserts "Banana" at index 1
