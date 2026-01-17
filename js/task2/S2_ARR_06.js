function activeUserNames(users) {
  return users
    .filter(u => u.active)
    .map(u => u.name.toUpperCase())
    .sort();
}

const users = [
  { id: 1, name: "Ana", active: true },
  { id: 2, name: "Luis", active: false },
  { id: 3, name: "Pedro", active: true }
];

console.log(activeUserNames(users)); // ["ANA","PEDRO"]
