"""Demonstrate negative slicing in Python."""

text = "Python"
numbers = [0, 1, 2, 3, 4, 5]

# Negative indices count from the end of a sequence.
print(text[-1])        # n: the last character
print(text[-3:])       # hon: the last three characters
print(text[:-2])       # Pyth: all but the last two characters
print(text[::-1])      # nohtyP: the reversed string

print(numbers[-4:-1])  # [2, 3, 4]
print(numbers[::-2])   # [5, 3, 1]