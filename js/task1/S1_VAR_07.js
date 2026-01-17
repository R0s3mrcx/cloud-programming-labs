function toNumberOrNull(x) {
  const n = +x;
  return Number.isNaN(n) ? null : n;
}

["12", "12.5", " 12 ", "12x", ""]
  .forEach(v => console.log(v, "=>", toNumberOrNull(v)));
