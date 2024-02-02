function solution(d, budget) {
    let answer = 0;
    const sortedList = d.sort((a, b) => a - b);
    for (let i = 0; i < d.length; i++) {
        const target = sortedList[i];
        if (budget < 0 || budget < target) continue;
        answer += 1;
        budget -= target;
    }
    return answer;
}