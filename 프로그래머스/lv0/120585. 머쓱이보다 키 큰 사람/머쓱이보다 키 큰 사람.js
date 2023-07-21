function solution(array, height) {
  let count = 0;
  for (const num of array) {
    if (num > height) count += 1;
  }
  return count;
}