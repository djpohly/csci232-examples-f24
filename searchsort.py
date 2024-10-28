# Returns the index of the first match of item
# Returns -1 if the item wasn't found
def linear_search(xx, item):
    i = 0
    while i < len(xx):
        if item == xx[i]:
            return i
        i = i + 1
    return -1


def binary_search(xx, item):
    ...
