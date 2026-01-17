def at_least(min_val):
    return lambda x: x >= min_val

nums = [1,5,10]
print(list(filter(at_least(5), nums)))
