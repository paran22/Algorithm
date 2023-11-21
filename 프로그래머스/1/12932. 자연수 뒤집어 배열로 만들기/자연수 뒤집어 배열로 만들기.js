function solution(n) {
    return String(n).split('').map(str => Number(str)).reverse();
}