function solution(n) {  
  var answer = 0;
  let sqrt = Math.ceil(Math.sqrt(n));
  for (let i = 1; i < sqrt; i++) {
    if (n % i === 0) answer += 2;
  }
  if (sqrt * sqrt === n) answer += 1;
  return answer;
}