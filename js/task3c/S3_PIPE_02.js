const compose = (...fns) => value =>
  fns.reduceRight((v, fn) => fn(v), value);

console.log(compose(add1, double)(3));
