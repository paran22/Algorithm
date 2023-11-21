function solution(absolutes, signs) {
    let answer = 0;
    for (i in absolutes) {
        if (signs[i]) {
            answer += absolutes[i];
            continue;
        }
        answer -= absolutes[i];
    }
    return answer;
}