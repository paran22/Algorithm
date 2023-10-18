function solution(my_string, queries) {
    let answer = my_string;
    for (query of queries) {
        let temp = '';
        let idx = 0;
        const [first, second] = query;
        answer.split('').map((str, index) => {
            if (index >= first && index <= second) {
                temp += answer[second - idx];
                idx += 1;
                return;
            }
            temp += answer[index]
        });
        answer = temp;
    }
    return answer;
}