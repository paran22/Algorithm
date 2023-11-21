function solution(n) {
    const sqrt = Math.sqrt(n);
    return sqrt === Math.floor(sqrt) ? (sqrt + 1) ** 2 : -1;
}