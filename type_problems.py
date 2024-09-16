def all_in_range(a,b, xx):
    i = 0
    all_were_in_range = True
    while i < len(xx):
        if xx[i] < a or xx[i] >= b:
            all_were_in_range = False
        i = i + 1
    return all_were_in_range

def at_least_one_in_range(a, b, xx):
    i = 0
    while i < len(xx):
        if a <= xx[i] < b:
            return True
        i = i + 1
    return False

def num_true(xx):
    i = 0
    count = 0
    while i < len(xx):
        if xx[i]:
            count = count + 1
        i = i + 1
    return count

def sum_string(xx):
    i = 0
    s = ""
    total = 0
    while i < len(xx):
        if i != 0:
            s = s + "+"
        s = s + str(xx[i])
        total = total + xx[i]
        i = i + 1
    s = s + "=" + str(total)
    return s

def evaluate_poly(coefficients, x):
    i = 0
    total = 0
    while i < len(coefficients):
        total = total + coefficients[i] * (x ** i)
        i = i + 1
    return total

def evaluate_poly2(coefficients, x):
    i = 0
    total = 0
    x_power = 1
    while i < len(coefficients):
        total = total + coefficients[i] * x_power
        x_power = x_power * x
        i = i + 1
    return total
