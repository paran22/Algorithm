function solution(n) {
    return String(n).split('').map((e) => Number(e)).reduce((a, b) => a + b);
}