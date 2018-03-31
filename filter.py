from itertools import ifilter

podcasts = ['The Podcast', 'Podcast inkubator', 'Nela Simic TV']

def long_name(name):
    return len(name) > 10

short1 = filter(long_name, podcasts)
short2 = ifilter(long_name, podcasts)

print(short1)
print(list(short1))
print(short2)
print (list(short2))
