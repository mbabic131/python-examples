# boolean
is_conor_comming_bact = True
print(type(is_conor_comming_bact))

if is_conor_comming_bact:
    print("Conor is comming back to MMA!")

# number
num = 10 # integer
print(type(num))
decimal = 3.14
print(type(decimal)) # float
complexnum = 2 + 3j
print(type(complexnum))

# string
name = "Conor"
r_name = reversed(name)
print(type(name))
print(r_name)

if isinstance(name, str):
    print("name variable is string")

# None
x = None  # No value will be assigned. Any valid datatype can be assigned later
print(x)

# converting data types
result = "15.45"
print(type(result))
result = float(result)
print(type(result))

sport = "MMA"
sport = list(sport)
print(sport)

# Lists (lists are mutable)
p4p = ["DJ", "DC", "Stipe", "GSP"]
p4p.append("Conor")
print(p4p)
for fighter in p4p:
    print(fighter)

# Tuples (similar to a list except that it is fixed-length and immutable)
ip_address = ('127.0.1.1', 8080)

# Dictionaries (A dictionary is a collection of key-value pairs)
matchups = {
    1: 'TJ vs. DJ',
    2: 'DC vs. Stipe',
    3: 'Cyborg vs. Nunes',
}

print(matchups)

# Set (A set is a collection of elements with no repeats and without insertion order but sorted order)
set_matchups = {'DC vs. Stipe', 'Cyborg vs. Nunes'}
if 'DC vs. Stipe' in set_matchups:
    print('Fight for the Heavyweight title.')