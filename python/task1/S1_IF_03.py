def normalize_name(value):
    if not value:
        return "Anonymous"
    name = value.strip()
    return name if name else "Anonymous"

tests = ["", " ", None, " Ola "]
for t in tests:
    print(normalize_name(t))
