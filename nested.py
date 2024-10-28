def matrix_rows(m):
    return len(m)

def is_square(m):
    rows = len(m)
    for row in m:
        if len(row) != rows:
            return False
    return True






def trace_square(m):
    # Matrix is square
    assert is_square(m)
    pass

def trace_any(m):
    pass






def sum_vector(xx):
    total = 0
    for x in xx:
        total += x
    return total

def sum_matrix(m):
    pass







def scaled_vector(xx, c):
    newvec = []
    for x in xx:
        newvec.append(c * x)
    return newvec

def scaled_matrix(m):
    pass
