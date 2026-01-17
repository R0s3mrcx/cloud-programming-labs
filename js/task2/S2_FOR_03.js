function sumUntil(nums, threshold) {
  let sum = 0;
  for (const n of nums) {
    if (sum + n > threshold) break;
    sum += n;
  }
  return sum;
}

console.log(sumUntil([2, 4, 6, 10], 10)); // 6
