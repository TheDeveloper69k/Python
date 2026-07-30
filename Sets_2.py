s = {1,2,5,7,9}
r = {2,3,5,8,9}
print(s.union(r))  # Output: {1, 2, 3, 5, 7, 8, 9} (the order may vary)
print(r.union(s))  # Output: {1, 2, 3, 5, 7, 8, 9} (the order may vary)
print(s.intersection(r))  # Output: {2, 5, 9} (the order may vary)
print(r.intersection(s))  # Output: {2, 5, 9} (the order may vary)

print(s.difference(r))  # Output: {1, 7} (the order may vary)
print(r.difference(s))  # Output: {3, 8} (the order may vary)

#The difference() method returns a set that contains the elements that are present in the first set but not in the second set. In this case, s.difference(r) returns {1, 7} because those elements are in s but not in r, while r.difference(s) returns {3, 8} because those elements are in r but not in s.