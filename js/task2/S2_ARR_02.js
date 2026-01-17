function unique(values) {
  const result = [];
  for (const v of values) {
    if (!result.includes(v)) {
      result.push(v);
    }
  }
  return result;
}

// test
console.log(unique([1, 2, 2, 3, 1, 4])); // [1,2,3,4]
