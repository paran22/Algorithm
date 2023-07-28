function solution(n) {
    let answer = 0;
    for (let i = 1; i < n + 1; i++) {
        if (Array(i).fill().map((_, index) => index + 1).filter((num) => i % num === 0).length > 2) {
            answer += 1;
        }
    }
    return answer;
}