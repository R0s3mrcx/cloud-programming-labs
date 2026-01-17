def group_by(items, key):
    result = {}
    for item in items:
        k = item.get(key)
        result.setdefault(k, []).append(item)
    return result

users = [{"name":"Ana","role":"admin"},{"name":"Bob","role":"user"}]
print(group_by(users, "role"))
