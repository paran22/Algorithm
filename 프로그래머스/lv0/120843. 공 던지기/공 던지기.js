function solution(numbers, k) {
    while (numbers.length < k * 2) {
        numbers = [...numbers, ...numbers]
    }
    return numbers[(k - 1) * 2];
}