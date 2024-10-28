def sum(xx) :
    # Sum of the first "i" elements of xx
    result_so_far = 0
    # Number of iterations completed
    # Number of elements added together
    i = 0
    while i < len(xx) :
        result_so_far = result_so_far + xx[i]
        i = i + 1
    assert i == len(xx)
    return result_so_far

def cat_all(xx) :
    # Concatenation of the first "i" elements of xx
    result_so_far = ""
    # Number of iterations completed
    # Number of elements concatenated together
    i = 0
    while i < len(xx) :
        result_so_far = result_so_far + xx[i]
        i = i + 1
    assert i == len(xx)
    return result_so_far

def join(sep, xx) :
    if len(xx) == 0 :
        return ''
    assert len(xx) >= 1
    result = xx[0]
    i = 1
    while i < len(xx) :
        result = result + sep + xx[i]
        i = i + 1
    assert i == len(xx)
    return result

def poly_to_str(coefficients) :
    poly = ''
    i = 0
    while i < len(coefficients) :
        if coefficients[i] != 0 :
            if poly != '' and coefficients[i] > 0 :
                poly = poly + '+'
            poly = poly + str(coefficients[i])
            if i > 0 :
                poly = poly + 'x'
            if i > 1 :
                poly = poly + '^' + str(i)
        i = i + 1
    assert i == len(coefficients)
    return poly

def binary_to_string(xx) :
    bin_num = ''
    i = 0
    while i < len(xx) :
        if xx[i] :
            bin_num = '1' + bin_num
        else :
            bin_num = '0' + bin_num
        i = i + 1
    return bin_num

def binary_to_int(bb) :
    result = 0
    b = 1
    i = 0
    while i < len(bb) :
        if bb[i] :
            result = result + b
        b = b * 2
        i = i + 1
    return result

def binary_increment(bb) :
    i = 0
    while i < len(bits) and bits[i] :
        bits[i] = False
        i = i + 1
    if i < len(bits) :
        bits[i] = True

def num_true(xx) :
    trues = 0
    i = 0
    while i < len(xx) :
        if xx[i] :
            trues = trues + 1
        i = i + 1
    return trues

def is_sorted(xx) :
    # A list with zero or one element is trivially sorted
    if len(xx) < 2 :
        return True
    assert len(xx) >= 2
    # Everything from index 0 to i exclusive is correctly ordered
    is_sorted = True
    # 
    i = 1
    while is_sorted and i < len(xx):
        is_sorted = xx[i-1] <= xx[i]
        i = i + 1
    assert (is_sorted == False) or (i == len(xx))
    return is_sorted
