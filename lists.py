# lists (An ordered collection of n values)
mma_stars = ['Conor McGregor', 'Holly Holm', 'Cris Cyborg', 'Stipe Miocic', 'John Jones']

boxing_stars = ['Floyd Mayweather', 'Canelo Alvarez', 'Vasly Lomachenko', 'Gennady Golovkin', 'Manny Pacquiao']
boxing_stars_nicks = ['Money', 'Cinnamon', 'Matrix', 'GGG', 'Pac-Mac']

# count elemnents in list
num_mma = mma_stars.count('Holly Holm')
print(num_mma)

# get index of list element
print(boxing_stars.index('Vasly Lomachenko'))

# sort list
mma_stars.sort()
print(mma_stars)

# reverse list
boxing_stars.reverse()
boxing_stars_nicks.reverse()
print(boxing_stars)

# append element to list
mma_stars.append('Mirko CroCop')
print(mma_stars.pop())

# List Comprehensions
squares = [x**2 for x in range(10)]
print(squares)

nums_combo = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(nums_combo)

boxing_stars_with_nicks = [star + ' - ' + boxing_stars_nicks[boxing_stars.index(star)] for star in boxing_stars]
print(boxing_stars_with_nicks)

from math import pi
num_pi = [str(round(pi, i)) for i in range(1, 6)]
print(num_pi)

# delete element from list
del boxing_stars[0]
print(boxing_stars)

# tuples (An ordered collection of n values of any type)
tpl = 1, 5, 'Paulie', 'Push', [1, 2, 'lay']
print(tpl)

# list with same string
duplicate_string = ['Thug Rose', 'Thug Rose', 'Thug Rose']
print(duplicate_string)

# list with multiple data types
multiple_types = ['String', 10, [12.14, 55]]
print(multiple_types)
