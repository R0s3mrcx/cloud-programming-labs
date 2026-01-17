def invert(obj):
    result = {}
    for k, v in obj.items():
        result.setdefault(v, []).append(k)
    return result

print(invert({"a":1,"b":2,"c":1}))
