def safe_add(a, b):
    result = a + b
    print("type:", type(result))
    return result

safe_add(10**30, 10**30)
