def compose(*fns):
    def run(x):
        for fn in reversed(fns):
            x = fn(x)
        return x
    return run

f = compose(lambda x: x+1, lambda x: x*2)
print(f(3))
