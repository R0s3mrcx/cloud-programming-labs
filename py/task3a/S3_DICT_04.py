def omit(d, keys):
    return {k: v for k, v in d.items() if k not in keys}


print(omit({"a": 1, "b": 2, "c": 3}, ["b"]))
