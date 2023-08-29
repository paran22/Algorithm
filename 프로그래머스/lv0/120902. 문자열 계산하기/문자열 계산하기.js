function solution(my_string) {
    const arr = my_string.split(' ');
    var answer = 0;
    var operator = '';
    for (i in arr) {
        const num = Number(arr[i]);
        if (i == 0) answer += num;
        if (!num) {
            operator = arr[i]
            continue;
        }
        if (operator === '+') answer += num;
        if (operator === '-') answer -= num;
    }
    return answer;
}