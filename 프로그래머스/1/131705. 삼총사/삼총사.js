function solution(number) {
    let answer = 0;
    for (let i = 0; i < number.length; i++) {
        for (let j = i + 1; j < number.length; j++) {
            for (let z = j + 1; z < number.length; z++) {
                const sum = number[i] + number[j] + number[z];
                if (sum === 0) answer += 1;
            }
        }
    }
    return answer;
}