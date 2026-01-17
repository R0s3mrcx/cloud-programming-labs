lines = ["INFO: user=42", "ERROR: x", "INFO: user=99"]

users = [
    int(line.split("=")[1])
    for line in lines
    if line.startswith("INFO")
]

print(users)
