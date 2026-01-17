def grade(score):
    if score < 0 or score > 100:
        return None
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

print(grade(85))
print(grade(120))
