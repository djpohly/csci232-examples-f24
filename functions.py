def double(x):
    return x * 2

def add(x, y):
    return x + y

def is_even(x):
    return x % 2 == 0
    # if x % 2 == 0:
    #     return True
    # else:
    #     return False

def leq(x, y):
    return x <= y


# Returns a new list
# ("map")
def apply_to_all(f, xx):
    # f is a function
    # xx is a list
    result = []
    for value in xx:
        result.append(f(value))
    return result


l = [2, 4, 5, 8, -3]

doubled = apply_to_all(double, l)
even = apply_to_all(is_even, l)
doubled_even = apply_to_all(is_even, apply_to_all(double, l))

print(doubled)
print(even)
print(doubled_even)


def filter(p, xx):
    result = []
    for x in xx:
        if p(x):
            result.append(x)
    return result

evens = filter(is_even, l)
print(evens)
# [2, 4, 8]



def reduce(f, xx, start):
    #      ^  
    result = start
    for x in xx:
        result = f(result, x)
    return result

def reduce2(f, xx):
    assert len(xx) > 0
    # if len(xx) == 1:
    #     return xx[0]

    result = xx[0]
    for x in xx[1:]:
        result = f(result, x)
    return result


the_sum = reduce(add, l, 0)
# 2 + 4 + 5 + 8 + -3 == 16
print(the_sum)
the_sum = reduce2(add, l)
print(the_sum)

def times(a, b):
    return a * b

the_product = reduce(times, l, 1)
print(the_product)
the_product = reduce2(times, l)
print(the_product)
