function solution(n) {
    const answer = [];
    let i = 2;
    while (i <= n) {
        if (n % i === 0) {
            if (!answer.includes(i)) answer.push(i);
            n /= i
            continue;
        }
        i += 1;
    }
    return answer.sort((a, b) => a - b);
}