function solution(s) {
    const arr = s.split(' ');
    let answer = 0;
    let temp = 0;
    for (e of arr) {
        if (e === 'Z') {
            answer -= temp;
            continue;
        }
        temp = Number(e);
        answer += Number(e);
    }
    return answer;
}