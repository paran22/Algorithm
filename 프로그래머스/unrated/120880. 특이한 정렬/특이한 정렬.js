function solution(numlist, n) {
    let sorted = numlist.map(num => [num, Math.abs(num - n)]).sort((a, b) =>  a[1] - b[1] || b[0] - a[0]);
    return sorted.map(num => num[0]);
}