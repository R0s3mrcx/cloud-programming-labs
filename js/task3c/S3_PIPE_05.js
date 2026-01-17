const pipe = (...fns) => value =>
  fns.reduce((v, fn) => fn(v), value);

const parse = line => {
  const [level, rest] = line.split(": ");
  return { level, user: rest.split("=")[1] };
};

const getInfoUsers = pipe(
  lines => lines.map(parse),
  items => items.filter(i => i.level === "INFO"),
  items => items.map(i => i.user)
);

console.log(
  getInfoUsers([
    "INFO: user=42",
    "ERROR: user=99",
    "INFO: user=7"
  ])
);
