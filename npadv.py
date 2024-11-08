import numpy as np

aa = np.random.randn(7, 5)
aa2 = aa.reshape(5, 7)

def mtimesv(m, v):
    assert m.ndim == 2
    assert v.ndim == 1
    assert m.shape[1] == v.shape[0]

    result = np.zeros(m.shape[0])
    # for r in range(m.shape[0]):
    #     for c in range(m.shape[1]):
    #         result[r] += m[r, c] * v[c]
    # return result
    
    for r in range(m.shape[0]):
        result[r] = sum(m[r] * v)
    return result

# Overwrite part of aa, starting at (r, c),
# with bb
def overwrite_part(aa, r, c, bb):
    ...


# Returns an array containing only those rows of
# aa which are in sorted order.
def sorted_rows(aa):
    ...
