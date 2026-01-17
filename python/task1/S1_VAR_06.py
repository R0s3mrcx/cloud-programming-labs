import math

def classify_number_like(x):
    if isinstance(x, float) and math.isnan(x):
        return "nan"
    if isinstance(x, (int, float)):
        return "number"
    return "not-a-number"

tests = [float("nan"), 0, "0", "abc", None]
for t in tests:
    print(t, classify_number_like(t))
