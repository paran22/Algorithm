function solution(n) {
    let answer = 1;
    let factorial = 1;
    while (factorial <= n) {
        answer += 1;
        factorial *= answer;
    }
    return answer - 1;
}