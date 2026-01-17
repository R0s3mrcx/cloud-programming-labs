people = [{"name":"Ana","age":30},{"name":"Bob","age":20}]
people.sort(key=lambda p: p["age"])
print(people)
