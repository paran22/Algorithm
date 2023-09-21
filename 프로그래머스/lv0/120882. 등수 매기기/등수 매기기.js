function solution(score) {
    const sumArr = score.map(item => item[0] + item[1]);
    const sorted = [...sumArr].sort((a, b) => b - a);
    return sumArr.map(item => sorted.indexOf(item) + 1)
}