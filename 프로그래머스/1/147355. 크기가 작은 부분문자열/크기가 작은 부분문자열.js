function solution(t, p) {
    let answer = 0;
    for (let i = 0; i < t.length - p.length + 1; i++) {
        const word = t.slice(i, i + p.length);
        if (Number(word) <= Number(p)) answer += 1;
    }
    return answer;
}