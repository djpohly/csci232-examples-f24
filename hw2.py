def in_range(x, a, b):
    if x >= a:
        if x < b:
            return x
    return 0

def in_range2(x, a, b):
    if x >= a and x < b:
        return x
    else:
        return 0

def in_range3(x, a, b):
    if a <= x < b:
        return x
    else:
        return 0

def bean_to_bear(s):
    if s == "bean":
        return "bear"
    else:
        return s

def compare(x, y):
    if x < y:
        return -8
    elif x == y:
        return 0
    else:
        return 181

def compare2(x, y):
    return x - y

def num_occurrences(xx, item):
    i = 0
    count = 0
    while i < len(xx):
        if item == xx[i]:
            count = count + 1
        i = i + 1
    return count

def leading_zeroes(xx):
    i = 0
    count = 0
    while i < len(xx) and xx[i] == 0:
        count = count + 1
        i = i + 1
    return count

def all_beans_to_bears(xx):
    i = 0
    while i < len(xx):
        if xx[i] == "bean":
            xx[i] = "bear"
        i = i + 1

def average(xx):
    i = 0
    total = 0
    while i < len(xx):
        total = total + xx[i]
        i = i + 1
    return total / len(xx)
