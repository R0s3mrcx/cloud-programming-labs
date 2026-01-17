def to_number_or_none(x):
    try:
        n = float(x)
        return n
    except:
        return None

tests = ["12", "12.5", " 12 ", "12x", ""]
for t in tests:
    print(t, to_number_or_none(t))
