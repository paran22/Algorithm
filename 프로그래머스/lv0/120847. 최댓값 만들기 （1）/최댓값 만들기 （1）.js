function solution(numbers) {
  const sorted = [...numbers].sort((a, b) => a - b);
  return sorted.at(-1) * sorted.at(-2);
}