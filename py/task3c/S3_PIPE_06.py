def pipe_safe(*fns):
    def run(x):
        try:
            for fn in fns:
                x = fn(x)
            return {"ok": True, "value": x}
        except Exception as e:
            return {"ok": False, "error": str(e)}
    return run


safe = pipe_safe(lambda x: int(x), lambda x: x * 2)
print(safe("5"))
print(safe("x"))
