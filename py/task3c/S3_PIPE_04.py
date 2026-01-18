def numbers_pipeline(values):
    for v in values:
        try:
            yield float(v.strip()) * 2
        except:
            continue


data = ["1", " x ", "2.5"]
print(sum(numbers_pipeline(data)))
