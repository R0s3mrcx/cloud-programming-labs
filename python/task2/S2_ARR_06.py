users = [
    {"id":1,"name":"Ana","active":True},
    {"id":2,"name":"Bob","active":False},
    {"id":3,"name":"Carla","active":True}
]

result = sorted([u["name"].upper() for u in users if u["active"]])
print(result)
