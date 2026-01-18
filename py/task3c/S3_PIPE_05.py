def parse_line(line):
    try:
        level, rest = line.split(":", 1)
        parts = dict(p.split("=") for p in rest.strip().split())
        return {"level": level, **parts}
    except:
        return None


def extract_users(lines):
    result = []
    for line in lines:
        parsed = parse_line(line)
        if parsed and parsed.get("level") == "INFO":
            try:
                result.append(int(parsed["user"]))
            except:
                pass
    return result


logs = [
    "INFO: user=42 action=login",
    "ERROR: user=x",
    "INFO: user=7 action=logout"
]

print(extract_users(logs))
