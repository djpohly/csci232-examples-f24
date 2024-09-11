def has_an_even(xx):
    # Does the list contain an even number?
    i = 0
    found_even = False
    while i < len(xx):
        if xx[i] % 2 == 0:
            found_even = True
        i = i + 1
    return found_even

def all_are_even(xx):
    i = 0
    found_odd = False
    while i < len(xx):
        if xx[i] % 2 != 0:
            found_odd = True
        i = i + 1
    return not found_odd

def all_same_type(xx):
    i = 1
    while i < len(xx):
        if type(xx[i]) != type(xx[0]):
            return False
        i = i + 1
    return True



# Prime sieve
sieve = [
    False, False, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True,
    True, True, True, True, True,
]

def print_true_indices(xx):
    i = 0
    while i < len(xx):
        if xx[i]:
            print(i)
        else:
            pass
        i = i + 1

def cross_off_multiples(xx, n):
    i = 0
    while i < len(xx):
        if xx[i] % n == 0:
            if xx[i]



