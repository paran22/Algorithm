function solution(sides) {
    let answer = 0;
    for (let i = 1; i < sides[0] + sides[1]; i++) {
        const arr = [...sides, i].sort((a, b) => a - b);
        if (arr[2] < arr[0] + arr[1]) answer += 1;
    }
    return answer;
}