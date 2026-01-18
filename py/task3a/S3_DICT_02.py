def merge_defaults(defaults, overrides):
    return {**defaults, **overrides}

defaults = {"a": 1, "b": {"x": 10}}
overrides = {"b": {"y": 20}}

merged = merge_defaults(defaults, overrides)
print(merged)  
