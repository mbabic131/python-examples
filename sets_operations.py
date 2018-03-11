# Union
union1 = {1, 2, 3, 4, 5}.union({3, 4, 5, 6, 7})
union2 = {1, 2, 3, 4, 5} | {3, 4, 5, 6, 7}
print(union1)
print(union2)

# Difference
diff1 = {2, 3, 4, 5, 6, 7}.difference({2, 3, 4, 5})
diff2 = {2, 3, 4, 5, 6, 7} - {2, 3, 4, 5}
print(diff1)
print(diff2)

# Existence check
isIn = 2 in {1, 2, 3}
notIn = 3 not in {1, 2, 3}
print(isIn)
print(notIn)

# Add and Remove
s = {5, 10, 15}
s.add(20)
print(s)

s.discard(5)
print(s)

s.remove(10)
print(s)

# Subset and superset
# c.issubset(a) tests whether each element of c is in a
# a.issuperset(c) tests whether each element of c is in a
a = {1, 2, 3, 4}
c = {1, 2}
print(c.issubset(a))
print(a.issuperset(c))

# If we want to get a unique elements from list, we can turn that list into set
ufc_events = ["UFC 221", "UFC 222", "UFC 224", "UFC 221", "UFC 222"]
print(ufc_events)
unique_events = set(ufc_events)
print(unique_events)

# Create list with unique elements from another list
unique_list = list(set(ufc_events))
print(unique_list)

from collections import Counter
counterA = Counter(['a', 'b', 'b', 'c'])
print(counterA)