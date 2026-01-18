people = [
    {"name": "Ana", "age": 30},
    {"name": "Bob", "age": 20},
    {"name": "Luis", "age": 25},
]

print("Before:", people)
people_sorted = sorted(people, key=lambda p: p["age"])
print("After:", people_sorted)
