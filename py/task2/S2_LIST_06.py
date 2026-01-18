def active_user_names(users):
    return sorted(
        [u["name"].upper() for u in users if u.get("active")]
    )

users = [
    {"id": 1, "name": "ana", "active": True},
    {"id": 2, "name": "bob", "active": False},
    {"id": 3, "name": "carlos", "active": True},
]

print(active_user_names(users))
