def get_path(obj, path, fallback=None):
    current = obj
    for key in path.split("."):
        if not isinstance(current, dict) or key not in current:
            return fallback
        current = current[key]
    return current


data = {"a": {"b": {"c": 10}}}
print(get_path(data, "a.b.c", None))
print(get_path(data, "a.b.x", "fallback"))
