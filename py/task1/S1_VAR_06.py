def to_int_or_none(s):
    try:
        if s is None:
            return None
        return int(s)
    except Exception:
        return None

tests = ["12", " 12 ", "12x", "", None]
for t in tests:
    print(t, "->", to_int_or_none(t))
