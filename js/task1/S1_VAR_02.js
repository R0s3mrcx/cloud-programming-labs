try {
  {
    let x = 10;
  }
  console.log(x);
} catch {
  console.log("let is block-scoped and not accessible outside");
}

try {
  {
    var y = 20;
  }
  console.log("var is accessible outside block:", y);
} catch (err) {
  console.log(err.message);
}
