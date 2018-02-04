# sets - containers only unique elements (An unordered collection of unique values. Items must be hashable.)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print("orange" in basket)

# dictionaries (An unordered collection of unique key-value pairs; keys must be hashable.)
event_info = {'city': 'Las Vegas', 'type': 'PPV', 'promtor': 'Showtime Boxing', 'id': 55}
print(event_info)

# add key value pair
event_info['copromotor'] = 'UFC'
print(event_info)

# delete key
print(event_info['id'])
del event_info['id']
print(event_info)

# lists keys
print(list(event_info.keys()))

print('type' in event_info)
print('fight' in event_info)
print('name' not in event_info)

# dict comprehensions
dic_nums = {x: x**2 for x in (2, 4, 6)}
print(dic_nums)

# loop through dictionaries
for k, v in event_info.items():
    print(k, v)

