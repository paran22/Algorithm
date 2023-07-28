function solution(array) {
    const max = [...array].sort((a, b) => a - b).at(-1);
    return [max, array.indexOf(max)];
}