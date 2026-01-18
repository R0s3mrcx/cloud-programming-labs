import re

normalize = pipe(
    str.strip,
    str.lower,
    lambda s: re.sub(r"\s+", " ", s)
)

print(normalize(" Ala   Ma   Kota "))
