const people = [
  { name: "Ana", age: 30 },
  { name: "Luis", age: 20 },
  { name: "Pedro", age: 25 }
];

people.sort((a, b) => a.age - b.age);

console.log(people);
