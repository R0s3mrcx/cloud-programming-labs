def grade(score):
    try:
        s = int(score)
    except (TypeError, ValueError):
        return None

    if s < 0 or s > 100:
        return None
    elif s >= 90:
        return "A"
    elif s >= 80:
        return "B"
    elif s >= 70:
        return "C"
    elif s >= 60:
        return "D"
    else:
        return "F"

tests = [59, 60, 69, 70, 89, 90, 100, 101]
for t in tests:
    print(t, grade(t))
