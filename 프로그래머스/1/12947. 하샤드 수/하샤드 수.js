function solution(x) {
    const sum = x.toString().split('').reduce((a, b) => a + parseInt(b), 0);
    return x % sum === 0;
}