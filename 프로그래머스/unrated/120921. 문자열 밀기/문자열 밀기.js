function solution(A, B) {
    let answer = 0;
    const aArr = A.split('');
    const bArr = B.split('');
    for (let i = 0; i < A.length; i++) {
        if (aArr.toString() === bArr.toString()) {
            return answer;
        }
        const last = aArr.pop();
        aArr.unshift(last);
        answer += 1;
    }
    return -1;
}