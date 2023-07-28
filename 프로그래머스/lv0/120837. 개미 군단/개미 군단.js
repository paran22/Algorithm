function solution(hp) {
  let answer = 0;
  const attack = [5, 3, 1];
  for (i of attack) {
    answer += Math.floor(hp / i);
    hp %= i;
  }
  return answer;
}