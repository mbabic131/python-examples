# empty dictionary
d = {}

matchups = {}
matchups['boxing'] = {'champion': 'Anthony Joshua', 'challanger': 'Joseph Parker'}
matchups['mma'] = {'champion': 'Tony Ferguson', 'challanger': 'Khabib Nurmagomedov'}

print(matchups)

# loop over dictionary
for key, value in matchups.items():
    print(key,value)
