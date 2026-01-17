import math

def inspect(value):
    return {
        "type": type(value).__name__,
        "isArray": isinstance(value, list),
        "isNull": value is None,
        "isNaN": isinstance(value, float) and math.isnan(value)
    }

values = [None, 0, [], {}, float("nan"), "hi", True, 3.14]
for v in values:
    print(inspect(v))
