function solution(before, after) {
    const beforeArr = before.split('').sort();
    const afterArr = after.split('').sort();
    for (i in beforeArr) {
        if (beforeArr[i] !== afterArr[i]) return 0;
    }
    return 1;
}