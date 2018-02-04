def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

fib_numbers = fib(2000)
print(fib_numbers)

def speakConor(line, opponent = 'Floyd Mayweather'):
    print(line + ' => to ' + opponent)

speakConor('Why you carring a school bag, you can\'t even read!')
speakConor('That\'s C.J Watson mate. I don\'t know who the f--- you are. No disrespect tho kid, keep hustling and stay in school', 'Draymond Green')


# The default value is evaluated only once. This makes a difference when the default is a mutable object such as a
# list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed
# to it on subsequent calls:
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# if you dont want the default to be shared between subsequent calls, you can write the function like this instead
def ff(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(ff(1))
print(ff(2))
print(ff(3))

# define function with arbitary arguments and keywords
def fightinfo(city, *arguments, **keywords):
    print('This figth is in ' + city)
    for ar in arguments:
        print(ar)
    for key in keywords:
        print(key + ': ' + keywords[key])

fightinfo("Las Vegas", "Connor McGregor vs. Floyd Mayweather", Promotor="Showtime", CoPromotor="UFC", Type="PPV")

def danasIntro(*arguments):
    sep = "-"
    return sep.join(arguments)

intro = danasIntro('reigning', 'defending', 'undisputed', 'ufc', '155', 'champion', 'notorious', 'conor', 'mcgregor')
print(intro)

# Lambda expressions
def make_incrementator(n):
    return lambda x: x + n

wins = make_incrementator(49)
print("Wins before Conor fight", wins(0))
print("Wins after Conor fight", wins(1))
