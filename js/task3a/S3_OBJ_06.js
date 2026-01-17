function groupBy(items, key) {
  const result = {};

  for (const item of items) {
    const value = item[key];
    if (!result[value]) {
      result[value] = [];
    }
    result[value].push(item);
  }
  return result;
}

const people = [
  { name: "Ana", city: "Lima" },
  { name: "Luis", city: "Cusco" },
  { name: "Pedro", city: "Lima" }
];

console.log(groupBy(people, "city"));
