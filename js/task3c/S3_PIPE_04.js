const pipe = (...fns) => value =>
  fns.reduce((v, fn) => fn(v), value);

const processNumbers = pipe(
  arr => arr.filter(v => !isNaN(v)),
  arr => arr.map(Number),
  arr => arr.map(n => n * 2),
  arr => arr.reduce((a, b) => a + b, 0)
);

console.log(processNumbers(["1", "x", "2", "3"]));
