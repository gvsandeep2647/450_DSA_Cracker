def getMinMax(a, n):
    min_number = float('inf')
    max_number = -1
    for i in a:
        if i > max_number:
            max_number = i
        if i < min_number:
            min_number = i

    return min_number, max_number
