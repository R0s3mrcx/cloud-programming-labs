const mapValues = (obj, fn) => {
  const result = {};
  for (const key in obj) {
    result[key] = fn(obj[key]);
  }
  return result;
};

console.log(mapValues({ a: 1, b: 2 }, x => x * 10));
