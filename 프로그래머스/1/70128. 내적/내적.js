function solution(a, b) {
  return a.reduce((prev, next, index) => prev + a[index] * b[index], 0);
}