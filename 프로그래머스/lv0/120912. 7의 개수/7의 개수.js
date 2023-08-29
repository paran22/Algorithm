function solution(array) {
    return array.map((num) => String(num).split('')).flat(2).filter((num) => num === '7').length;
}