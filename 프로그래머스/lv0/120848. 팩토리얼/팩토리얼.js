function solution(n) {
    const factorial = (num) => {
        if (num === 1) return 1;
        return factorial(num - 1) * num;
    };
    let answer = 1;
    while (factorial(answer) <= n) {
        answer += 1;
    }
    return answer - 1;
}