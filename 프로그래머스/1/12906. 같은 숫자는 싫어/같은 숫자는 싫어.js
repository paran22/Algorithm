function solution(arr) {
    let answer = [];
    for (num of arr) {
        if (answer[answer.length - 1] === num) continue;
        answer.push(num);
    }
    return answer;
}