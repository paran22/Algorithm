function solution(num_list, n) {
    const answer = [];
    let array = [];
    for (index in num_list) {
        array.push(num_list[index]);
        console.log(array)
        if (index % n === n - 1) {
            answer.push(array);
            array = [];
        }
    }
    return answer;
}