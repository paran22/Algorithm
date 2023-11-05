function solution(quiz) {
    const answer = [];
    for (q of quiz) {
        const operator = q.includes(" + ") ? " + " : " - "
        const temp1 = q.split(operator);
        const temp2 = temp1[1].split(" = ");
        const arr = [temp1[0], ...temp2].map(str => Number(str));
        const result = operator === " + " ? arr[0] + arr[1] : arr[0] - arr[1];
        answer.push(result === arr[2] ? "O" : "X")
    }
    return answer;
}

