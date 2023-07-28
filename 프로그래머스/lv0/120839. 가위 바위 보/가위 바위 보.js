function solution(rsp) {
    let answer = '';
    for (i of rsp) {
        answer += i == 2 ? 0 : i == 0 ? 5 : 2;
    }
    return answer;
}