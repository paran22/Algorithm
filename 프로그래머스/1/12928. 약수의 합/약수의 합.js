function solution(n) {
    if (n < 2) return n;
    let answer = 1 + n;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        const quotient = n / i;
        if (quotient === Math.floor(quotient)) 
            answer += (i === quotient ? i : i + quotient);
    }
    return answer;
}