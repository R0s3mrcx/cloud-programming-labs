def compose(*fns):
    def run(x):
        for fn in reversed(fns):
            x = fn(x)
        return x
    return run


f1 = lambda x: x + 1
f2 = lambda x: x * 2

print(pipe(f1, f2)(3))
print(compose(f1, f2)(3))
