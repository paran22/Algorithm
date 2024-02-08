function solution(t, p) {
    let array = [];
    for (let i = 0; i < t.length - p.length + 1; i++) {
        array.push(t.slice(i, i + p.length));
    }
    return array.filter(str => Number(str) <= Number(p)).length;
}