function solution(array, n) {
    array.sort();
    const distanceArr = array.map(num => Math.abs(num - n));
    const index = distanceArr.indexOf(Math.min(...distanceArr));
    return array[index];
}