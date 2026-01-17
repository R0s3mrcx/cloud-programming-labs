def day_name(n):
    days = {
        1: "Monday", 2: "Tuesday", 3: "Wednesday",
        4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"
    }
    return days.get(n)

print(day_name(3))
print(day_name(9))
