function get(obj, path, fallback) {
  const keys = path.split(".");
  let current = obj;

  for (const key of keys) {
    if (current == null || !(key in current)) {
      return fallback;
    }
    current = current[key];
  }
  return current;
}

const data = { a: { b: { c: 42 } } };
console.log(get(data, "a.b.c", null));
console.log(get(data, "a.x.c", "missing"));
