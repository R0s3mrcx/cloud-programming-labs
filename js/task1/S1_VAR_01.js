var city = "Lima";
let age = 26;
const isStudent = true;

const rows = [
  ["city", city, typeof city],
  ["age", age, typeof age],
  ["isStudent", isStudent, typeof isStudent],
];

console.table(rows);
