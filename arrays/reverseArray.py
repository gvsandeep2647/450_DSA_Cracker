def reverseArray(arr, m):
    reversed_part = arr[m + 1:]
    final_array = arr[:m] + reversed_part[::-1]
    return final_array
