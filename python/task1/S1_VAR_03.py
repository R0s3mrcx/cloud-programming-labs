user = {"name": "Ala", "tags": []}
user["tags"].append("admin")
user["tags"].append("editor")

print(user)

try:
    user = {}
except Exception as e:
    print(e)
