function solution(s) {
    const length = s.length;
    if (length !== 4 && length !== 6) return false;
    for (char of s) {
        if (Number.isNaN(Number(char))) return false;
    }
    return true;
}