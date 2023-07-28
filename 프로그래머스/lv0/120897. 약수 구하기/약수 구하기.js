function solution(n) {
    return [...Array(n).keys()].map((num) => num + 1).filter((num) => n % num === 0);
}