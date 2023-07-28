function solution(my_string, num1, num2) {
    const array = Array.from(my_string);
    [array[num1], array[num2]] = [array[num2], array[num1]];
    return array.join('');
}