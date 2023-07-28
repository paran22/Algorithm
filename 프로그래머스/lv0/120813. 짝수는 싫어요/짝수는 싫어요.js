function solution(n) {
  return [...Array(n + 1).keys()].filter((num) => num % 2);
}