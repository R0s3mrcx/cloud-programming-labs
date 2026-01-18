def normalize_name(x):
    if not x:
        return "Anonymous"

    name = x.strip()
    if name == "":
        return "Anonymous"

    return name

print(normalize_name(""))
print(normalize_name(" "))
print(normalize_name(None))
print(normalize_name(" Ola "))
