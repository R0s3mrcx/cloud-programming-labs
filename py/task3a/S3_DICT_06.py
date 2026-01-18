def group_by(items, key):
    groups = {}
    for item in items:
        value = item.get(key)
        groups.setdefault(value, []).append(item)
    return groups

people = [
    {"name": "Ana", "city": "Lima"},
    {"name": "Bob", "city": "NY"},
    {"name": "Luis", "city": "Lima"},
]

print(group_by(people, "city"))
