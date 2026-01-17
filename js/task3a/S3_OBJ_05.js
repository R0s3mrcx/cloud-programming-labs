function invert(obj) {
  const result = {};

  for (const key in obj) {
    const value = obj[key];
    if (value in result) {
      result[value] = [].concat(result[value], key);
    } else {
      result[value] = key;
    }
  }
  return result;
}

console.log(invert({ a: 1, b: 2, c: 1 }));

