def process(arr):
    nums = []
    for x in arr:
        try:
            nums.append(int(x))
        except:
            pass
    return sum(n*2 for n in nums)

print(process(["1","x","2"]))
