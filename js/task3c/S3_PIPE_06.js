const pipeSafe = (...fns) => value => {
  try {
    return {
      ok: true,
      value: fns.reduce((v, fn) => fn(v), value)
    };
  } catch (error) {
    return { ok: false, error };
  }
};

const risky = x => {
  if (x < 0) throw new Error("Negative!");
  return x * 2;
};

console.log(pipeSafe(risky)(5));
console.log(pipeSafe(risky)(-1));
