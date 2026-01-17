def chunk(arr, size):
    if size <= 0:
        return None
    return [arr[i:i+size] for i in range(0, len(arr), size)]

print(chunk([1,2,3,4,5], 2))
