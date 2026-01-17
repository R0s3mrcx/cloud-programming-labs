def type_label(value):
    if value is None:
        return "null"
    return type(value).__name__

tests = [None, 42, "42", True, {}, [], lambda x: x]
for t in tests:
    print(t, "=>", type_label(t))
