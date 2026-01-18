def at_least(min_value):
    return lambda n: n >= min_value


nums = [1, 5, 10, 15]
filtered = list(filter(at_least(10), nums))
print(filtered)
