function solution(left, right) {
    var answer = 0;    
    for (let i = left; i < right + 1; i++) {
        const count = getFactorsCount(i);
        if (count % 2 === 1) {
            answer -= i;
            continue;
        }
        answer += i;
    }
    return answer;
}

function getFactorsCount(num) {
    let count = 0;
    for (let i = 1; i < Math.sqrt(num) + 1; i++) {
        if (num % i === 0) {
            count += num / i === i ? 1 : 2;
        }
    }
    return count;
}