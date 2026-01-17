def clean_numbers(arr):
    result = []
    for x in arr:
        try:
            n = float(x)
            result.append(int(n) if n.is_integer() else n)
        except:
            pass
    return result

print(clean_numbers([" 1 ", "x", "2"]))
