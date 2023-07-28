function solution(numbers, direction) {
    if (direction === 'left') {
        const first = numbers.shift();
        numbers.push(first);
        return numbers;
    }
    if (direction === 'right') {
        const last = numbers.pop();
        numbers.unshift(last);
        return numbers;
    }
}