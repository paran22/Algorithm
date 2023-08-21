function solution(my_string) {
    let answer = 0;
    let temp = '';
    for (str of my_string) {
        if (Number(str) > -1) {
            temp += str;
            continue;
        }
        answer += Number(temp);
        temp = '';
    }
    return answer + Number(temp);
}