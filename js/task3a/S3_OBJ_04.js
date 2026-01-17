function omit(obj, keys) {
  const result = { ...obj };
  for (const key of keys) {
    delete result[key];
  }
  return result;
}

console.log(omit({ a: 1, b: 2, c: 3 }, ["b"]));
