def stats(nums):
    if not nums:
        return None

    total = sum(nums)
    return {
        "min": min(nums),
        "max": max(nums),
        "sum": total,
        "avg": total / len(nums)
    }


print(stats([1, 2, 3]))
print(stats([-5, 0, 5]))
print(stats([]))
