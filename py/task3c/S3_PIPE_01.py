def pipe(*fns):
    def run(x):
        for fn in fns:
            x = fn(x)
        return x
    return run

f = pipe(lambda x: x + 1, lambda x: x * 2)
print(f(3))
