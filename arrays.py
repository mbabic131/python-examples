from array import *

my_array = array('i', [1,2,3,4,5])

print(my_array[1])
print(my_array[4])

# append value to array
my_array.append(6)
# insert value to array (index, value)
my_array.insert(0,0)

# extend array
my_extend_array = array('i', [7,8,9])
my_array.extend(my_extend_array)

# remove element form array
my_array.remove(3)

# remove last element from array
my_array.pop()

for i in my_array:
    print(i)

# count number of occurrences
countnum = my_array.count(2)
print('Number 2 count: ' + str(countnum))

# array to list converting
arrayToList = my_array.tolist()
print(arrayToList)
