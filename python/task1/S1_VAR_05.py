def is_array(value):
    return isinstance(value, list)

print(is_array([1,2,3]))
print(is_array({"a":1}))
