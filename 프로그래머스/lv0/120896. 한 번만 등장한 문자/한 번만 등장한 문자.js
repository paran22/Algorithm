function solution(s) {
    const arr = s.split('');
    const set = new Set(arr);
    const temp = [];
    for (s of set) {
        if (arr.filter(e => e === s).length === 1) temp.push(s);
    }
    return temp.sort().join('');
}