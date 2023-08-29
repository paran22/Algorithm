function solution(my_str, n) {
    const answer = [];
    while (my_str.length > 0) {
        const endIndex = my_str.length > n ? n : my_str.length;
        answer.push(my_str.slice(0, endIndex));
        my_str = my_str.slice(endIndex);
    }
    return answer;
}