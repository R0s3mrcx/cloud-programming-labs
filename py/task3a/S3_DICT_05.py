def invert(d):
    result = {}
    for k, v in d.items():
        if v not in result:
            result[v] = [k]
        else:
            result[v].append(k)
    return result

print(invert({"a": 1, "b": 2, "c": 1}))
