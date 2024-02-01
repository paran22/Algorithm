function solution(n) {
    const ternaryStr = n.toString(3);
    const reversedStr = ternaryStr.split('').reverse().join('');
    return parseInt(reversedStr, 3);
}