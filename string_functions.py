a = "Hiten"

print(a.upper())  # Output: HITEN
print(a.lower())  # Output: hiten
print(a.capitalize())  # Output: Hiten
print(a.title())  # Output: Hiten
print(a.swapcase())  # Output: hITEN
print(a.strip())  # Output: Hiten (no leading/trailing whitespace to remove)
print(a.replace("H", "J"))  # Output: Jiten
print(a.startswith("Hi"))  # Output: True
print(a.endswith("en"))  # Output: True
print(a.find("t"))  # Output: 3 (index of 't')
print(a.count("i"))  # Output: 1 (number of occurrences of 'i')
print(a.isalpha())  # Output: True (all characters are alphabetic)
print(a.isdigit())  # Output: False (not all characters are digits)
print(a.isalnum())  # Output: True (all characters are alphanumeric)
print(a.split("i"))  # Output: ['H', 'ten'] (splits the string at 'i')
print(a.join(["Hello", "World"]))  # Output: HelloHitenWorld (joins the list with 'Hiten' in between)
print(a.replace("H", "J").upper())  # Output: JITEN (replaces 'H' with 'J' and converts to uppercase)
