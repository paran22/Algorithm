function solution(array) {
    let occurence = Array(1000).fill(0);
    for (num of array) {
        occurence[num] += 1;
    }
    const max = Math.max(...occurence);
    const first = occurence.indexOf(max);
    const last = occurence.lastIndexOf(max);
    return first !== last ? -1 : first;
}