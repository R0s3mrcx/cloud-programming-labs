const atLeast = min => n => n >= min;

console.log([1, 5, 10, 15].filter(atLeast(10)));
