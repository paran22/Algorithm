function solution(cipher, code) {
  let answer = '';
  for (i in cipher) {
    if (i % code === code - 1) {
      answer += cipher[i];
    }
  }
  return answer;
}
