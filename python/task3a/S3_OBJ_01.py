def get(obj, path, fallback=None):
    current = obj
    for key in path.split("."):
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return fallback
    return current

data = {"a": {"b": {"c": 42}}}
print(get(data, "a.b.c", "X"))
print(get(data, "a.b.x", "fallback"))
