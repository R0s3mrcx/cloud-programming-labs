def sample_function():
    return "I am a function"

values = {
    "int": 42,
    "float": 3.14,
    "str": "hello",
    "bool": True,
    "none": None,
    "list": [1, 2, 3],
    "tuple": (1, 2, 3),
    "dict": {"a": 1},
    "set": {1, 2, 3},
    "function": sample_function
}

print(f"{'NAME':<10} {'VALUE':<20} {'TYPE':<30} {'TYPE NAME'}")
print("-" * 80)

for name, value in values.items():
    print(
        f"{name:<10} "
        f"{str(value):<20} "
        f"{str(type(value)):<30} "
        f"{type(value).__name__}"
    )
