function safeAdd(a, b) {
  if (
    Number.isInteger(a) &&
    Number.isInteger(b) &&
    (Math.abs(a) > Number.MAX_SAFE_INTEGER ||
     Math.abs(b) > Number.MAX_SAFE_INTEGER)
  ) {
    console.log("Using BigInt");
    return BigInt(a) + BigInt(b);
  }
  console.log("Using Number");
  return a + b;
}

console.log(safeAdd(10, 20));
