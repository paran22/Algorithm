function solution(numbers) {
    const array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    return array.filter(num => !numbers.includes(num)).reduce((a, b) => a + b);
}