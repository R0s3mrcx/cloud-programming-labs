def count_occurrences(values):
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    return counts

print(count_occurrences(["a", "b", "a", "c", "b", "a"]))
