def clean_numbers(values):
    result = []
    for v in values:
        try:
            result.append(float(v.strip()))
        except (AttributeError, ValueError):
            continue
    return result

print(clean_numbers([" 1 ", "x", "2"]))
print(clean_numbers(["3.5", " ", "4"]))
