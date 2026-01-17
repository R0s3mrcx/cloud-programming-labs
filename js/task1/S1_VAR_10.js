function inspect(value) {
  return {
    type: typeof value,
    isArray: Array.isArray(value),
    isNull: value === null,
    isNaN: Number.isNaN(value),
  };
}

[null, 0, NaN, [], {}, "hello", undefined, () => {}]
  .forEach(v => console.log(inspect(v)));
