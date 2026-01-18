def calc(a, op, b):
    try:
        a = float(a)
        b = float(b)
    except (TypeError, ValueError):
        return None

    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return None
            return a / b
        case _:
            return None


print(calc(5, "+", 3))
print(calc(5, "-", 3))
print(calc(5, "*", 3))
print(calc(5, "/", 0))
print(calc(5, "/", 2))
print(calc(5, "%", 2))
