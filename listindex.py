xx = [2, 3, 5, 7, 11]

for x in xx:
    print(x + 1)


def num_occurrences(xx, n):
    i = 0
    count = 0
    while i < len(xx):
        if xx[i] == n:
            count += 1
        i += 1

    return count


def num_occurrences(xx, n):
    count = 0
    for x in xx:
        if x == n:
            count += 1

    return count


def num_occurrences(xx, n):
    count = 0
    for i in range(len(xx)):
        if xx[i] == n:
            count += 1

    return count


def evaluate_poly(coeffs, x):
    total = 0
    for i in range(len(coeffs)):
        total += coeffs[i] * (x ** i)
    return total

def evaluate_poly(coeffs, x):
    total = 0
    x_power = 1
    for c in coeffs:
        total += c * x_power
        x_power *= x
    return total
