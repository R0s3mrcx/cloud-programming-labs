def is_truthy(v):
    return bool(v)

tests = [0, 1, "", "0", [], [0], {}, None]

for t in tests:
    print(f"{t!r:>6} -> {is_truthy(t)}")
