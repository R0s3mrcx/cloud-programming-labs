def stats(nums):
    if not nums:
        return None
    return {
        "min": min(nums),
        "max": max(nums),
        "avg": sum(nums) / len(nums)
    }

print(stats([1,2,3,4]))
