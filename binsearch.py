def binary_search(xx, n):
    # Assume xx is sorted least to greatest
    # First index which might contain n
    start = 0
    # 1 more than the last index which might contain n
    stop = len(xx)

    while start < stop:
        # Index of the middle element
        mid = (start + stop) // 2
        middle_value = xx[mid]

        if middle_value == n:
            return mid
        elif middle_value < n:
            start = mid + 1
        else:
            assert middle_value > n
            stop = mid
    return None
