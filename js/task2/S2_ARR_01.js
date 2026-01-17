function cleanNumbers(arr) {
  return arr
    .map(v => Number(v.trim()))
    .filter(v => !Number.isNaN(v));
}

console.log(cleanNumbers([" 1 ", "x", "2", " 3.5 "])); // [1, 2, 3.5]
