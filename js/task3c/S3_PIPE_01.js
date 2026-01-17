const pipe = (...fns) => value =>
  fns.reduce((v, fn) => fn(v), value);

const add1 = x => x + 1;
const double = x => x * 2;

console.log(pipe(add1, double)(3));
