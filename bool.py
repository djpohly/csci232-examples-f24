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
primes = [True] * 100
primes[0] = False
primes[1] = False

def print_true_indices(xx):
    i = 0
    while i < len(xx):
        if xx[i]:
            print(i)
        else:
            pass
        i = i + 1

def cross_off_multiples_old(xx, n):
    i = n + 1
    while i < len(xx):
        if i % n == 0:
            xx[i] = False
        i = i + 1

def cross_off_multiples(xx, n):
    i = n * 2
    while i < len(xx):
        xx[i] = False
        i = i + n

def sieve(xx):
    p = 2
    while p < len(xx):
        if xx[p]:
            cross_off_multiples(xx, p)
        else:
            pass
        p = p + 1
    print_true_indices(xx)


fortytwo = [False, True, False, True, False, True]

def binary_increment(bb):
    i = 0
    while i < len(bb) and bb[i]:
        bb[i] = False
        i = i + 1
    if i >= len(bb):
        bb.append(True)
    else:
        bb[i] = True
