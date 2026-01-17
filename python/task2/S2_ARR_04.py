def flatten1(arr):
    result = []
    for x in arr:
        if isinstance(x, list):
            result.extend(x)
        else:
            result.append(x)
    return result

print(flatten1([1,[2,3],[4],5]))
