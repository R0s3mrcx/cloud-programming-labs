def merge_defaults(defaults, overrides):
    merged = defaults.copy()
    merged.update(overrides)
    return merged

print(merge_defaults({"a":1,"b":2}, {"b":9,"c":3}))
