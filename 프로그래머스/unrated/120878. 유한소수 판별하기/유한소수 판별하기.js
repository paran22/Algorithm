function solution(a, b) {
    const bArr = [];
    const arr = [];
    let i = 2;
    while (a > 1 && b > 1 && i < Math.max(a, b) + 1) {
        if (a % i === 0 && b % i === 0) {
            a /= i;
            b /= i;
        }
        i += 1;
    }
    while (b % 2 === 0) {
        b /= 2;
    }
    while (b % 5 === 0) {
        b /= 5;
    }
    return b === 1 ? 1 : 2;
}