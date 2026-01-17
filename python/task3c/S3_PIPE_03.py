import re

normalize = pipe(
    str.strip,
    str.lower,
    lambda s: re.sub(r"\s+", " ", s)
)

print(normalize("  Hola    Mundo  "))
