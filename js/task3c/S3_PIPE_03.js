const pipe = (...fns) => value =>
  fns.reduce((v, fn) => fn(v), value);

const normalize = pipe(
  s => s.trim(),
  s => s.toLowerCase(),
  s => s.replace(/\s+/g, " ")
);

console.log(normalize("  HELLO   World  "));
