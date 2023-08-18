function solution(i, j, k) {
    return Array(j-i+1).fill(0).map((_, index) => `${index + i}`.split('')).flat(2).filter((e) => e == `${k}`).length;
}