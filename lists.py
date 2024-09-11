# Calculate the sum of a list

def total(xx):
    i = 0
    count = 0

    while i < len(xx):
        count = count + xx[i]
        i = i + 1

    return count


def count_even(xx):
    i = 0
    count = 0
    while i < len(xx):
        if xx[i] % 2 == 0:
            count = count + 1

        i = i + 1
        
    return count
