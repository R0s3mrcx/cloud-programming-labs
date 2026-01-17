def omit(obj, keys):
    return {k:v for k,v in obj.items() if k not in keys}

print(omit({"a":1,"b":2,"c":3}, ["b"]))
