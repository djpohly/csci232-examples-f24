def matrix_rows(m):
    return len(m)

def is_square(m):
    for row in m:
        if len(row) != len(m):
            return False
    return True


def trace_square(m):
    assert is_square(m)



def list_sum(xx):
    total = 0
    for x in xx:
        total += x
    return total
