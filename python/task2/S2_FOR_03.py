def sum_until(nums, threshold):
    total = 0
    for n in nums:
        if total + n > threshold:
            break
        total += n
    return total

print(sum_until([2, 4, 6, 10], 12))
